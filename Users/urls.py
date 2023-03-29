from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('users/',views.add_user),
    path('users/',views.delete_user)
]