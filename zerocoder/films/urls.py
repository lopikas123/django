from django.urls import path
from .views import film_create_view, film_list_view

urlpatterns = [
    path('create/', film_create_view, name='film_create'),
    path('', film_list_view, name='film_list'),
]