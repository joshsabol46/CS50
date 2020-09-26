from django.urls import path

from . import views

# app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit/<str:title>", views.edit, name="edit"),

    # wiki/<str:title> [name='entry']
    # wiki/Add [name='addEntry']
    # wiki/random [name='random']
    # wiki/edit [name='edit']
]
