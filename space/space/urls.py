"""
URL configuration for space project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appln import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form'),
    
    path('', views.home, name='home'),
    path('descrip1/', views.descrip1, name='descrip1'),
    path('descrip2/', views.descrip2, name='descrip2'),
    path('descrip3/', views.descrip3, name='descrip3'),
    path('card/', views.card, name='card'),
    path('info/', views.info, name='info'),
    path('fullsearch/', views.fullsearch, name='fullsearch'),
    path('login/', views.login, name='login'),
    path('payment/', views.payment, name='payment'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('upi/', views.upi, name='upi'),
    path('Home/',views.home)
    
    
]
