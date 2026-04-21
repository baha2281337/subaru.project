from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Car, Category
from .serializers import (
    CarSerializer,
    CategorySerializer,
    RegisterSerializer,
    UserSerializer,
)


def home_page(request):
    featured_models = [
        {
            "name": "Outback",
            "tagline": "Adventure-ready wagon with all-weather confidence.",
            "price": "From $29,010",
        },
        {
            "name": "Forester",
            "tagline": "Practical family SUV with strong visibility and AWD.",
            "price": "From $31,415",
        },
        {
            "name": "WRX",
            "tagline": "Performance sedan with rally DNA and turbo power.",
            "price": "From $34,920",
        },
    ]
    highlights = [
        "Symmetrical All-Wheel Drive on every key model",
        "Driver assistance and safety-first positioning",
        "Structured landing page for a Subaru-inspired course project",
    ]
    return render(
        request,
        "home.html",
        {
            "featured_models": featured_models,
            "highlights": highlights,
        },
    )


def cars_page(request):
    cars = Car.objects.all().select_related("category")
    return render(request, "cars/cars.html", {"cars": cars})


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    def get_queryset(self):
        queryset = Car.objects.all()

        year = self.request.query_params.get('year')
        category = self.request.query_params.get('category')

        if year:
            queryset = queryset.filter(year=year)

        if category:
            queryset = queryset.filter(category_id=category)

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
        return Response(
            {
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({"user": UserSerializer(request.user).data})


@api_view(['GET'])
def api_home(request):
    return Response({"message": "API works"})
