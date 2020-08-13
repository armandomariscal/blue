from django.shortcuts import render, redirect, get_object_or_404
from main.models import Movie


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home.html', context)
