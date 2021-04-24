from django.shortcuts import render
from .models import Movie, Director, Studio, Genre
from django_filters import views
from django.views import generic
from django.urls import reverse_lazy

def show_index(request):
    context = {
        'total_movie': Movie.objects.all().count(),
        'total_directors': Director.objects.all().count(),
        'total_studio': Studio.objects.all().count(),
        'total_genre': Genre.objects.all().count(),
    }
    return render(request, 'movieapp/index.html', context)

class MovieListView(views.FilterView):
    model = Movie
    filterset_fields = ['title','director','studio','released_date','genre','asin']

class MovieCreateView(generic.CreateView):
    model = Movie
    fields = ['title','prefix','subtitle','slug','director','studio','released_date','genre','cover_image','review','asin']
    success_url = reverse_lazy('movie-list')

class MovieUpdateView(generic.UpdateView):
    model = Movie
    fields = ['title', 'prefix', 'subtitle', 'slug', 'director', 'studio', 'released_date', 'genre', 'cover_image',
              'review', 'asin']
    success_url = reverse_lazy('movie-list')
