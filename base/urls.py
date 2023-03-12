from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.logoutPage, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('room/<int:pk>', views.room, name='room'),
    path('user-profile/<int:pk>', views.userPage, name='user-profile'),
    path('update-room/<int:pk>', views.updateRoom, name='update-room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('delete-room/<int:pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<int:pk>', views.deleteMessage, name='delete-message'),
]
