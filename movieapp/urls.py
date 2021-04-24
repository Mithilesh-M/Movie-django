from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movie/create/', views.MovieCreateView.as_view(), name= 'movie-create'),
]