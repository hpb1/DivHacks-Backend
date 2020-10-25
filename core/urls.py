from django.urls import path
from .views import TreeView, CarbonFootprintView
urlpatterns = [
    path('tree/view/', TreeView.as_view()),
    path('tree/add/', TreeView.as_view()),
    path('tree/delete/<str:pk>/', TreeView.as_view()),
    path('carbon/', CarbonFootprintView.as_view()),
]
