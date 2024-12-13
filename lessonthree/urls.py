
from django.urls import path

from . import views

urlpatterns = [
    path("", views.three, name="three"),
]