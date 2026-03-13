from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
 path('', views.cars_list, name='cars_list'),
 path('', views.home),
 path('cars/', views.cars_list),
 path('api/cars/', views.cars_api),
 path('', views.home),
 path('cars/', views.get_cars),
 path('cars/<int:car_id>/', views.get_car),
 path('register/', views.register),
 path('profile/', views.profile),
 path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
 path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Subaru API",
      default_version='v1',
      description="API for Subaru project",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

