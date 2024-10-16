from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.http import JsonResponse
from .models import Contact

def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Save to database
            Contact.objects.create(name=name, email=email, message=message)
            return JsonResponse({'status': 'success', 'message': 'Your message has been sent.'})
        else:
            return JsonResponse({'status': 'error', 'message': "You didn't fill the form. Please fill out all fields."})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})



# Create your views here.

def home(request):
    return render(request,"home.html")

def descrip1(request):
    return render(request, 'descrip1.html')

def descrip2(request):
    return render(request, 'descrip2.html')

def descrip3(request):
    return render(request, 'descrip3.html')

def card(request):
    return render(request, 'card.html')

def info(request):
    return render(request, 'info.html')

def fullsearch(request):
    return render(request, 'fullsearch.html')

def login(request):
    return render(request, 'login.html')

def payment(request):
    return render(request, 'payment.html')

def search(request):
    return render(request, 'search.html')


def upi(request):
    return render(request, 'upi.html')

def signup(request):
    return render(request, 'signup.html')
