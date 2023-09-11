from django.urls import path
from . import views

urlpatterns = [
path("Question", views.index, name="index"),
]
