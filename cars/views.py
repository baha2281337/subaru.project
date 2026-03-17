from django.shortcuts import render
from .models import Car
from django.http import JsonResponse
from .serializers import CategorySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from .models import Category



def home(request):
    return render(request, "home.html")


def cars_list(request):
    cars = Car.objects.all()
    return render(request, "cars.html", {"cars": cars})

def cars_api(request):
    cars = list(Car.objects.values())
    return JsonResponse(cars, safe=False)

def cars_list(request):
    cars = Car.objects.all()
    return render(request, "cars/cars.html", {"cars": cars})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
cars = [
    {"id": 1, "name": "Subaru WRX", "engine": "2.0 Turbo", "type": "Sedan"},
    {"id": 2, "name": "Subaru Forester", "engine": "2.5", "type": "SUV"},
    {"id": 3, "name": "Subaru Outback", "engine": "2.5", "type": "Crossover"},
    {"id": 4, "name": "Subaru BRZ", "engine": "2.0", "type": "Coupe"},
]

@api_view(['GET'])
def get_cars(request):
    return Response({"cars": cars})


@api_view(['GET'])
def home(request):
    return Response({"message": "Subaru API работает"})

@api_view(['GET'])
def get_car(request, car_id):
    for car in cars:
        if car["id"] == car_id:
            return Response(car)
    return Response({"error": "Car not found"}, status=404)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(user).data,
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({"user": UserSerializer(request.user).data})
    