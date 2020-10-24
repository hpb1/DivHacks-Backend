from django.urls import path
from .views import TreeView
urlpatterns = [
    path('view/', TreeView.as_view()),
    path('add/', TreeView.as_view()),
    path('delete/<str:pk>/', TreeView.as_view()),
]
