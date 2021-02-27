from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="ptfHome"),
    path("about/", views.about,name="Aboutme"),
    path("blog/", views.blog,name="BLOG"),


]