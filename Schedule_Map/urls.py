from django.urls import path
from . import views

app_name = "Schedule_Map"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:yr>", views.setSched, name="setSched")
]