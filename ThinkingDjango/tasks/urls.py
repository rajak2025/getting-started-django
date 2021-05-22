from django.urls import path

from . import views

#Explicitly invoking tasks app views
app_name = "tasks"

urlpatterns = [
     path("",views.index, name = "index"),
     path("add", views.add, name = "add")
]