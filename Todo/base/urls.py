from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("delete/<int:id>", views.Delete, name="Delete"),
    path("incomplete/<int:id>", views.Incomplete, name="Incomplete"),
    path("complete/<int:id>", views.Complete, name="Complete"),
]
