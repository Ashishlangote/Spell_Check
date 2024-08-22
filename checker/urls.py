from django.urls import path

from . import views

urlpatterns = [
    path('', views.SpellCheckView.as_view(), name='index'),
]