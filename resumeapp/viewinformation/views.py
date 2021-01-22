from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'viewinformation/index-sidebar-dark-scheme.html')

# Create your views here.
