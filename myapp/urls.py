from django.urls import path
from.import views

urlpatterns = [
    # path('', views.first, name='first'),
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('tables', views.tables, name='tables'),
    path('delete_multiple/', views.delete_multiple, name='delete_multiple'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('portfolio-details', views.portfolio_details, name='portfolio-details'),
    path('privacy', views.privacy, name='privacy'),
    path('service-details', views.service_details, name='service-details'),
    path('starter-page', views.starter_page, name='start-page'),
    path('terms', views.terms, name='terms'),
    path('page-404', views.page_404, name='page-404'),
    path('django-forms', views.django_forms, name='django-forms')
]