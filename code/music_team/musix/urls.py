from django.urls import path
from .views import RoomView
urlpatterns = [
    path('sound', RoomView.as_view()),
]