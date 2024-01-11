from django.urls import path, include
from .views import functionsRooms

users_url = [
    path('create_room', functionsRooms.create_room, name='create_room'),
    path('get_rooms', functionsRooms.Room, name='get_rooms'),
    path('update_room', functionsRooms.update_room, name='update_room'),
    path('delete_room', functionsRooms.delete_room, name='delete_room'),
]
urlpatterns = users_url