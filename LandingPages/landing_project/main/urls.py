from django.urls import path
from . import views

urlpatterns = [
    path("", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("interest/", views.interest_form, name="interest_form"),
]
