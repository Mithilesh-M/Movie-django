from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_index, name='index'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movie/create/', views.MovieCreateView.as_view(), name= 'movie-create'),
    path('movie/update/<int:pk>', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movie/detail/<int:pk>', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/delete/<int:pk>', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('director/', views.DirectorListView.as_view(), name='director-list'),
    path('director/create/', views.DirectorCreateView.as_view(), name='director-create'),
    path('director/update/<int:pk>', views.DirectorUpdateView.as_view(), name='director-update'),
    path('director/detail/<int:pk>', views.DirectorDetailView.as_view(), name='director-detail'),
    path('director/delete/<int:pk>', views.DirectorDeleteView.as_view(), name='director-delete'),
    path('studios/', views.StudioListView.as_view(), name='studio-list'),
    path('studio/create/', views.StudioCreateView.as_view(), name='studio-create'),
    path('studio/update/<int:pk>', views.StudioUpdateView.as_view(), name='studio-update'),
    path('studio/delete/<int:pk>', views.StudioDeleteView.as_view(), name='studio-delete'),
    path('studio/detail/<int:pk>', views.StudioDetailView.as_view(), name='studio-detail'),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genre/create/', views.GenreCreateView.as_view(), name='genre-create'),
]