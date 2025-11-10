from django.urls import path
from . import views

urlpatterns = [

    path("people_list/<int:id>", views.get_character, name = "people")
    path("people_list/", views.get_people_list, name = "people_list")
]