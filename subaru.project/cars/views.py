from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Car, Category
from .serializers import (
    CarSerializer,
    CategorySerializer,
    RegisterSerializer,
    UserSerializer
)


def home_page(request):
    return render(request, "home.html")


def cars_page(request):
    cars = Car.objects.all()
    return render(request, "cars/cars.html", {"cars": cars})



class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def get_queryset(self):
        queryset = Car.objects.all()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(year=year)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



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
    return Response({
        "user": UserSerializer(request.user).data
    })

@api_view(['GET'])
def api_home(request):
    return Response({"message": "API работает"})