from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('createproject/',views.create_project)
]