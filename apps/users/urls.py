from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    CreateUserApiView,
    UserListApiView,
    UserDetailApiView,
    UserUpdateApiView,
    UserDeleteApiView
)


urlpatterns = [
    path('auth', CustomTokenObtainPairView.as_view(), name="access_token"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('create', CreateUserApiView.as_view(), name="create"),
    path('all', UserListApiView.as_view(), name="user_list"),
    path('detail/<uuid:user_id>', UserDetailApiView.as_view(), name="user_detail"),
    path('update/<uuid:user_id>', UserUpdateApiView.as_view(), name="update_user"),
    path('delete/<uuid:user_id>', UserDeleteApiView.as_view(), name="delete_user"),
]