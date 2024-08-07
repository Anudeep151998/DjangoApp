from django.shortcuts import render
from django.http import HttpResponse 
 

# Create your views here.
def home(request): 

    return render(request, 'itreporting/home.html')

def about(request): 

    return render(request, 'itreporting/about.html')

def contact(request): 

    return render(request, 'itreporting/contact.html')
