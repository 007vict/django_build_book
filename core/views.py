from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from core.models import Movie

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    model = Movie



