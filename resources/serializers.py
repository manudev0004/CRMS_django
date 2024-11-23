from rest_framework import serializers
from .models import DeviceResource
from .models import Metric

class DeviceResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceResource
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

