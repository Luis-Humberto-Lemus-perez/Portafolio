from django.urls import path
from . import views

from rest_framework import routers
from .task import TaskViewSet
from . import user

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, 'tasks')
urlpatterns = [
    path("", views.getRoutes),
    path("login", views.login),
    path("register", user.register),
    path("login1", user.login),
    path("profile", user.profile),
    path("logout", user.logout),
    path("delete/<int:pk>", user.delete),
    path("view", user.view),
    path("notes", views.getSuperUserInfo),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += router.urls