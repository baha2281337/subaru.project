from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    CarViewSet,
    CategoryViewSet,
    api_home,
    cars_page,
    home_page,
    profile,
    register,
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'cars', CarViewSet, basename='car')


urlpatterns = [
    path('', home_page, name='home'),
    path('models/', cars_page, name='cars_page'),
    path('api/', api_home, name='api_home'),
    path('api/', include(router.urls)),
    path('api/register/', register, name='register'),
    path('api/profile/', profile, name='profile'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
