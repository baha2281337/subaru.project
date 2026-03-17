from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    CarViewSet,
    CategoryViewSet,
    register,
    profile,
    api_home,
    home_page,
    cars_page
)


router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'categories', CategoryViewSet)



schema_view = get_schema_view(
    openapi.Info(
        title="Subaru API",
        default_version='v1',
        description="API for Subaru project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [

    path('', home_page),
    path('cars-page/', cars_page),

    path('api/', include(router.urls)),
    path('api/', api_home),

    path('api/register/', register),
    path('api/profile/', profile),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),


    path('admin/', admin.site.urls),
]