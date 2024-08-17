from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http.response import HttpResponse
from app import views as main


router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.empty_resp),
    path('api/', main.modelPredict.as_view())
]


