# ~/my_django_project/ajsbsd/ajsbsdDotnet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_view, name='hello_world'),
]
