#from django.shortcuts import render

# Create your views here.
from django.views import generic

class HomeView(generic.DetailView):
    template_name = "home/main.html"

