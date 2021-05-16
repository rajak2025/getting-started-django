from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test_route", views.test_route, name ="test_route"),
    path("<str:name>", views.greet, name="greet")
    #name of the route at the end
]