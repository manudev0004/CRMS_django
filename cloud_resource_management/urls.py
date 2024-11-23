"""
URL configuration for cloud_resource_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from resources.views import DeviceResourceViewSet
from resources.views import MetricViewSet
from resources.views import LiveMetricsView
from resources.views import ChartDataView
from resources.views import HistoryDataView
# from resources import views

router = DefaultRouter()
router.register('resources', DeviceResourceViewSet)
router.register('metrics', MetricViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # This serves the API
    path('api/live-metrics/', LiveMetricsView.as_view(), name='live-metrics'),
    path('api/chart-data/', ChartDataView.as_view(), name='chart_data'),
    path('api/history/', HistoryDataView.as_view(), name='history_data'),
]
