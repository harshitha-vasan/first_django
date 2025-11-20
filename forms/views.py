from django.shortcuts import render, redirect
from .models import formDetails

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']
        print(name, email, phone, comment)
        data= formDetails(name=name, email=email, phone=phone, comment=comment)
        data.save()
    return render(request, 'forms/index.html')

def content(request):
    data=formDetails.objects.all()
    return render(request, 'forms/content.html', {'datas': data})

def update(request, id):
    data=formDetails.objects.get(id=id)
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']

        existingData=formDetails.objects.get(id=id)
        existingData.name=name
        existingData.email=email
        existingData.phone=phone
        existingData.comment=comment
        return redirect('forms/content')
    return render(request, 'forms/update.html')
    
def delete(request, id):
    data=formDetails.objects.get(id=id)
    data.delete()
    return redirect ('content')

# Create your views here.
