from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'cash/index.html')

def about(request):
    return render(request, 'cash/about.html')

def contact(request):
    return render(request, 'cash/contact.html')
