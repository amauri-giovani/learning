from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class Home(ListView):
    model = Article
    template_name = 'home.html'
