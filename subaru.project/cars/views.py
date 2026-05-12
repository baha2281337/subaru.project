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
            "name": "2026 Outback",
            "type": "Adventure Wagon",
            "image": "img/2026-outback.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26OBK_SUV_Pod3_xl",
            "tagline": "A redesigned adventure wagon with a stronger outdoor profile.",
            "highlights": ["2026", "AWD", "Adventure"],
        },
        {
            "name": "2026 Forester",
            "type": "Compact SUV",
            "image": "img/2026-forester.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26_FOR_SUV_Pod2",
            "tagline": "Everyday SUV comfort with practical space and confident traction.",
            "highlights": ["2026", "SUV", "Family fit"],
        },
        {
            "name": "2026 Crosstrek",
            "type": "Compact Crossover",
            "image": "img/2026-crosstrek.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26_CTK_SUV_Pod1",
            "tagline": "A compact crossover for city routes, rough roads, and weekend plans.",
            "highlights": ["2026", "Compact", "AWD"],
        },
        {
            "name": "2026 Ascent",
            "type": "Three-Row SUV",
            "image": "img/2026-ascent.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26_ASC_SUV_Pod4",
            "tagline": "A three-row SUV built for passengers, cargo, and longer drives.",
            "highlights": ["2026", "3 rows", "Family SUV"],
        },
        {
            "name": "2026 Solterra",
            "type": "Electric SUV",
            "image": "img/2026-solterra.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26SOL_SUV_Pod5_xl",
            "tagline": "An electric SUV with quiet power and all-weather positioning.",
            "highlights": ["2026", "EV", "AWD"],
        },
        {
            "name": "2026 Uncharted",
            "type": "Electric Crossover",
            "image": "img/2026-uncharted.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26UNC_SUV_xl",
            "tagline": "A new electric crossover aimed at compact, modern utility.",
            "highlights": ["2026", "New model", "EV"],
        },
        {
            "name": "2026 Trailseeker",
            "type": "Electric SUV",
            "image": "img/2026-trailseeker.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/201_26TSK_SUV_xl",
            "tagline": "A new electric SUV with adventure-focused proportions.",
            "highlights": ["2026", "New model", "EV"],
        },
        {
            "name": "2026 Impreza",
            "type": "Hatchback",
            "image": "img/2026-impreza.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/26_IMP_gallery_01",
            "tagline": "A compact hatchback with useful space and standard AWD character.",
            "highlights": ["2026", "Hatchback", "AWD"],
        },
        {
            "name": "2026 WRX",
            "type": "Performance Sedan",
            "image": "img/2026-wrx.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/26_WRX_features_hero_gallery_1",
            "tagline": "Turbocharged performance with a sharper road-focused stance.",
            "highlights": ["2026", "Turbo", "Sport"],
        },
        {
            "name": "2026 BRZ",
            "type": "Sports Coupe",
            "image": "img/2026-brz.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/26_BRZ_hero_gallery_1",
            "tagline": "A lightweight rear-drive sports coupe for focused driving.",
            "highlights": ["2026", "Coupe", "Manual feel"],
        },
        {
            "name": "2025 Legacy",
            "type": "Sedan",
            "image": "img/2025-legacy.jpg",
            "image_credit": "Subaru official image",
            "image_source": "https://s7d1.scene7.com/is/image/scomv2/25_LEG_gallery_1",
            "tagline": "A midsize sedan entry from the 2025 model year.",
            "highlights": ["2025", "Sedan", "AWD"],
        },
    ]
    shopping_tools = [
        {"title": "Build & Price", "text": "Compare trims and shape a configuration."},
        {"title": "Search Inventory", "text": "Browse available vehicles by model."},
        {"title": "Special Offers", "text": "See current shopping prompts in one place."},
        {"title": "Find a Retailer", "text": "Start from a local dealer-style entry point."},
    ]
    vehicle_groups = [
        {"name": "Hybrid", "text": "Balanced efficiency for daily driving."},
        {"name": "Electric", "text": "Battery-powered SUV capability."},
        {"name": "Gas", "text": "Core crossovers, wagons, and sedans."},
        {"name": "Wilderness", "text": "Rugged appearance and outdoor positioning."},
    ]
    brand_points = [
        {
            "title": "All-weather focus",
            "text": "The page keeps Subaru's familiar confidence-first positioning without copying official wording.",
        },
        {
            "title": "Safety-led shopping",
            "text": "Model cards and calls to action stay centered on the practical reasons buyers compare vehicles.",
        },
        {
            "title": "Adventure utility",
            "text": "Wide imagery, outdoor color, and clean navigation create the same broad category feel.",
        },
    ]
    return render(
        request,
        "home.html",
        {
            "featured_models": featured_models,
            "shopping_tools": shopping_tools,
            "vehicle_groups": vehicle_groups,
            "brand_points": brand_points,
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
