from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core_backend.models import Usuario
from voluptuous.schema_builder import Required
from backend.utils import validate_data

@api_view(['GET']) 
@permission_classes([AllowAny])
def get_users(request):
    users = Usuario.objects.all()
    return Response([{'nombre':user.nombre, 'apellido':user.apellido, 'identificador':user.identificador} for user in users])

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    data = validate_data({
        Required('nombre'):str,
        Required('apellido'):str,
        Required('identificador'):int,
    }, request.data)
    user = Usuario.objects.create(nombre=data['nombre'], apellido=data['apellido'], identificador=data['identificador'])
    user.save()
    return Response('Usuario creado exitosamente')

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request):
    data = validate_data({
        Required('nombre'):str,
        Required('apellido'):str,
        Required('identificador'):int,
    }, request.data)
    user = Usuario.objects.get(identificador=data['identificador'])
    user.nombre = data['nombre']
    user.apellido = data['apellido']
    user.save()
    return Response('Usuario actualizado exitosamente')

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request):
    data = validate_data({
        Required('identificador'):int,
    }, request.data)
    user = Usuario.objects.get(identificador=data['identificador'])
    user.delete()
    return Response('Usuario eliminado exitosamente')

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user(request):
    data = validate_data({
        Required('identificador'):int,
    }, request.data)
    user = Usuario.objects.get(identificador=data['identificador'])
    return Response({'nombre':user.nombre, 'apellido':user.apellido, 'identificador':user.identificador})
