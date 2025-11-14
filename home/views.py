from django.shortcuts import render
from django.views.generic import TemplateView
def home_view(request):
    return render(request, 'home/home.html')
def about_view(request):
    return render(request, 'home/about.html')