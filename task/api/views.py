from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/v1/token',
        '/api/v1/token/refresh',
        '/api/v1/apps',
        
    ]
    return JsonResponse(routes,safe=False)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from task.models import App
from .serializers import AppModelSerializer
from .permission import ReadOnlyOrAdminPermission

class AppModelListView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppModelSerializer
    # permission_classes = [IsAuthenticated]


class AppModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = App.objects.all()
    serializer_class = AppModelSerializer
    permission_classes = [ReadOnlyOrAdminPermission]