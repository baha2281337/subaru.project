from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet


urlpatterns = [
 path('', views.cars_list, name='cars_list'),
 path('', views.home),
 path('cars/', views.cars_list),
 path('api/cars/', views.cars_api),
]


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
]



