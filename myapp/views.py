from django.shortcuts import render, redirect, HttpResponse
from .models import contactDetails, registerDetails
from .forms import productDetailsForm
from functools import wraps
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.pip insta

# when @ isued, it is decorator,when this method used, it will naviagte to any page only when we login that is why this is used
def login_required(view_func):
    @wraps(view_func)
    def wrapped_func(request, *args, **kwargs): 
        if not request.session.get('is_logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapped_func

@csrf_exempt
def register(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password']

        data=registerDetails(user_name=user_name, email=email, password=password)
        data.save()
        return redirect('login')
    return render(request, 'register.html')

@csrf_exempt
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            user=registerDetails.objects.get(email=email)
            if user.password==password:
                request.session['email']=email
                request.session['is_logged_in'] = True
                return redirect('index')
            else:
                print('Invalid Username or Incorrect Password' )
        except:
            print('Invalid Username or Incorrect Password' )
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def first(request):
    return HttpResponse('This is my first Django project')

@csrf_exempt
@login_required
def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        screenshot = request.FILES.get('screenshot')
        session_id=request.session.get('email')
        # print(name, email, phone, subject, message)
        data= contactDetails(name=name, email=email, phone=phone, subject=subject, message=message, screenshot=screenshot, session_id=session_id)
        data.save()
        return redirect('tables')
    return render(request, 'index.html')

@login_required
def tables(request):
    data=contactDetails.objects.all()
    for i in data:
        print(i.name)
        print(i.screenshot)
    search_query = request.GET.get('search', '')

    data=contactDetails.objects.filter(
        Q(name__icontains=search_query) |
        Q(email__icontains=search_query) |
        Q(phone__icontains=search_query) |
        Q(subject__icontains=search_query) |
        Q(message__icontains=search_query)
    )
    return render(request,'tables.html', {'datas': data, 'search_query': search_query} )
 
@csrf_exempt
@login_required
def delete_multiple(request):
    if request.method == 'POST':
        selected_id = request.POST.getlist('selected_items')
        contactDetails.objects.filter(id__in=selected_id).delete()
        
    return redirect('tables')

@csrf_exempt
@login_required
def update(request, id):
    data=contactDetails.objects.get(id=id)
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']

        existing_data=contactDetails.objects.get(id=id)
        existing_data.name=name
        existing_data.email=email
        existing_data.phone=phone
        existing_data.subject=subject
        existing_data.message=message
        existing_data.save()
        return redirect('tables')
    return render(request, 'update.html', {'data': data})

@login_required
def delete(request, id):
    data=contactDetails.objects.get(id=id)
    data.delete()
    return redirect('tables')


@login_required
def portfolio_details(request):
    return render(request, 'portfolio-details.html')

@login_required
def privacy(request):
    return render(request, 'privacy.html')

@login_required
def service_details(request):
    return render(request, 'service-details.html')

@login_required
def starter_page(request):
    return render(request, 'starter-page.html')

@login_required
def terms(request):
    return render(request, 'terms.html')

@login_required
def page_404(request):
    return render(request, '404.html')

def django_forms(request):
    form= productDetailsForm()
    if request.method =='POST':
        data=productDetailsForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'django-forms.html', {'form':form})

