from django.shortcuts import render
from datetime import datetime

def portfolio(request):
    return render(request, 'index.html', {'year': datetime.now().year})

def projects(request):
    return render(request, 'projects.html', {'year': datetime.now().year})

def contact(request):
    return render(request, 'contact.html', {'year': datetime.now().year})