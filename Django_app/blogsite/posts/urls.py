from django import path, include
from . import views
urls = {
    path('',views.check_connection())
}