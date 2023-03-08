from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('', views.home, name='home'),
    path('room/<int:pk>', views.room, name='room'),
    path('update-room/<int:pk>', views.updateRoom, name='update-room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('delete-room/<int:pk>', views.deleteRoom, name='delete-room')
]
