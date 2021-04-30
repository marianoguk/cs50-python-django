from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.by_title, name="by_title"),
    path("search", views.search_by_title, name="search_by_title"),
    path("random", views.random_page, name="random_page"),
    path("create", views.create_page, name="create_page"),

]
