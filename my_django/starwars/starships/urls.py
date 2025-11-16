from django.urls import path
from . import views

urlpatterns = [
    path("starship/<int:id>/", views.get_starship, name="starship_detail"),
    path("starships/", views.get_starships_list, name="starships_list")
]