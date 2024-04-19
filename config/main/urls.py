from django.urls import path
from .views import *

urlpatterns = [
    path('', GameListCreateAPIView.as_view(), ),
    path('<int:pk>/', GameRetrieveUpdateDestroyAPIView.as_view(), ),
]
