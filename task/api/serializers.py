from rest_framework import serializers
from task.models import App

class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
