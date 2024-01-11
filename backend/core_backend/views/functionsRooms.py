from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from models import Sala
from voluptuous.schema_builder import Required
from backend.utils import validate_data

@api_view(['GET'])
@permission_classes([AllowAny])
def Room(request): 
    rooms = Sala.objects.all()
    response = []
    for room in rooms:
        response.append({'id': room.id,
        'nombre': room.nombre, 
        'tamaño': room.tamaño, 
        'ubicacion': room.ubicacion, 
        'aforo': room.aforo})
        return Response(response)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_room(request):
    data = validate_data({
        Required('nombre'): str, 
        ('tamaño'): int, 
        ('ubicacion'): str,
        ('aforo'): int
    }, request.data)
    if 'tamaño' not in data:
        data['tamaño'] = None
    if 'ubicacion' not in data:
        data['ubicacion'] = None
    if 'aforo' not in data:
        data['aforo'] = None
    
    room = Sala.objects.create(nombre=data['nombre'], tamaño=data['tamaño'], ubicaccion = data['ubicacion'], aforo = data['aforo'])
    room.save()
    return Response('Sala creada exitosamente')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_room(request):
    data = validate_data({
        Required('id'): int,
        ('nombre'): str,
        ('tamaño'): int,
        ('ubicacion'): str,
        ('aforo'): int
    }, request.data)
    try:
        room = Sala.objects.get(id=data['id'])
        if 'nombre' in data:
            room.nombre = data['nombre']
        if 'tamaño' in data:
            room.tamaño = data['tamaño']
        if 'ubicacion' in data:
            room.ubicacion = data['ubicacion']
        if 'aforo' in data:
            room.aforo = data['aforo']
        room.save()
        return Response('Sala actualizada exitosamente')
    except:
        return Response('La sala no existe', status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_room(request):
    data = validate_data({
        Required('id'): int
    }, request.data)
    try:
        room = Sala.objects.get(id=data['id'])
        room.delete()
        return Response('Sala eliminada exitosamente', status=status.HTTP_200_OK)
    except:
        return Response('La sala no existe', status=status.HTTP_404_NOT_FOUND)
