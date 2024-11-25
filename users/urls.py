from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserDestroyAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    # user urlpatterns
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', never_cache(UserCreateAPIView.as_view()), name='user-create'),
    path('<int:pk>/delete/', UserDestroyAPIView.as_view(), name='user-delete'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),

    # token urlpatterns
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
