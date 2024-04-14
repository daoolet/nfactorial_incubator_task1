from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("planets/", views.get_planets, name="planets"),
    path("people/", views.get_people, name="people"),
    path("starships/", views.get_starships, name="starships"),
]