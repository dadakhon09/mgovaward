from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from users.views import UserLogin, UserLogout, UserCreate, UserListAPIView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('create/', UserCreate.as_view(), name='create-user'),
    path('list/all/', UserListAPIView.as_view(), name='users-list'),
]

