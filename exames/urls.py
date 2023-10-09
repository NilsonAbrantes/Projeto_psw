from django.urls import path

from . import views

urlpatterns = [
    path("solicitar_exames/", view.solicitar_exames, name="solicitar_exames"),
]
