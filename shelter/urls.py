from django.urls import path
from .views import ShelterView, NearbyShelters

urlpatterns = [
    path('view/', ShelterView.as_view()),
    path('add/', ShelterView.as_view()),
    path('modify/<str:pk>/', ShelterView.as_view()),
    path('delete/<str:pk>/', ShelterView.as_view()),
    path('nearby/', NearbyShelters.as_view()),
]
