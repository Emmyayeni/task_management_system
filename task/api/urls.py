from django.urls import path
from . import views 
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import re_path
from rest_framework import permissions
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from .views import *
urlpatterns = [
    path('',views.getRoutes),
    path('api_schema/', get_schema_view(
        title='Task Schema',
        description='Guide for task management system api '
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='task/docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('apps/', AppModelListView.as_view(), name='apps'),
    path('app/<int:pk>/', AppModelDetailView.as_view(), name='app-detail'),
    
]
