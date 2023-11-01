
from django.urls import path
from . import views

# http://127.0.0.1:8000/ client       : ana sayfa
# http://127.0.0.1:8000/client/home    : ana sayfa
# http://127.0.0.1:8000/client/filmler : film listesi


urlpatterns = [
    path('', views.index),
    path('list', views.filmler,),
    path('<film_adi>', views.details,),
    path('kategori/<int:category_id>', views.getMoviesByCategoryId),
    path('kategori/<str:category_name>',
         views.getMoviesByCategory, name='movies_by_category'),



]
