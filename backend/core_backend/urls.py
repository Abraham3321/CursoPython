from django.urls import path, include
from .views import functionsRooms
from .views import functions_clients

users_url = [
    path('create_room', functionsRooms.create_room, name='create_room'),
    path('get_rooms', functionsRooms.Room, name='get_rooms'),
    path('update_room', functionsRooms.update_room, name='update_room'),
    path('delete_room', functionsRooms.delete_room, name='delete_room'),
    path('create_user', functions_clients.create_user, name='create_user'),
    path('get_users', functions_clients.get_users, name='get_users'),
    path('update_user', functions_clients.update_user, name='update_user'),
    path('delete_user', functions_clients.delete_user, name='delete_user'),
    path('get_user', functions_clients.get_user, name='get_user'),
]
urlpatterns = users_url