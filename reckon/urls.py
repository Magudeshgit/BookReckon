from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import modelPredict

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', modelPredict.as_view())
]
