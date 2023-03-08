from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'),
    path('details/<int:id>', views.details, name='details'),
]