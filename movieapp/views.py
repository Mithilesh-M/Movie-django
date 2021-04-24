from django.shortcuts import render
from .models import Movie, Director, Studio, Genre

def show_index(request):
    context = {
        'total_movie': Movie.objects.all().count(),
        'total_directors': Director.objects.all().count(),
        'total_studio': Studio.objects.all().count(),
        'total_genre': Genre.objects.all().count(),
    }
    return render(request, 'movieapp/index.html', context)
