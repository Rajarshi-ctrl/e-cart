from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user/", views.user, name="user"),
    path("my_cart/", views.my_cart, name="my_cart"),
    path("search/", views.search, name="search"),
]
