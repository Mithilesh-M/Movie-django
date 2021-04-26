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

class MovieDetailView(generic.DetailView):
    model = Movie

class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-list')

class DirectorListView(views.FilterView):
    model = Director
    filterset_fields = ['first_name','middle_name','last_name','phone','website','birthday','gender']

class DirectorCreateView(generic.CreateView):
    model = Director
    fields = ['first_name','middle_name','last_name','phone','website','birthday','gender']
    success_url = reverse_lazy('director-list')

class DirectorUpdateView(generic.UpdateView):
    model = Director
    fields = ['first_name', 'middle_name', 'last_name', 'phone', 'website', 'birthday', 'gender']
    success_url = reverse_lazy('director-list')

class DirectorDetailView(generic.DetailView):
    model = Director

class DirectorDeleteView(generic.DeleteView):
    model = Director
    success_url = reverse_lazy('director-list')

class StudioListView(views.FilterView):
    model = Studio
    filterset_fields = ['title','prefix','website','slug']

class StudioCreateView(generic.CreateView):
    model = Studio
    fields = ['title','prefix','website','slug']
    success_url = reverse_lazy('studio-list')

class StudioUpdateView(generic.UpdateView):
    model = Studio
    fields = ['title', 'prefix', 'website', 'slug']
    success_url = reverse_lazy('studio-list')

class StudioDeleteView(generic.DeleteView):
    model = Studio
    success_url = reverse_lazy('studio-list')

class StudioDetailView(generic.DetailView):
    model = Studio

class GenreListView(views.FilterView):
    model = Genre
    filterset_fields = ['title','slug']
