from django.shortcuts import render
from .models import Car
from django.http import JsonResponse
from .serializers import CategorySerializer



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