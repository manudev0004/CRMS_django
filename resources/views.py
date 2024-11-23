from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from datetime import datetime, timedelta
import psutil

from .models import DeviceResource, Metric
from .serializers import DeviceResourceSerializer, MetricSerializer


class MetricViewSet(ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class DeviceResourceViewSet(ModelViewSet):
    queryset = DeviceResource.objects.all()
    serializer_class = DeviceResourceSerializer


# class SystemMetrics:
#     """
#     Helper class to encapsulate system metric fetching logic.
#     """

#     @staticmethod
#     def get_cpu_usage():
#         return psutil.cpu_percent(interval=0.1)

#     @staticmethod
#     def get_memory_usage():
#         memory = psutil.virtual_memory()
#         return f"{memory.used / (1024 ** 3):.2f} GB"

#     @staticmethod
#     def get_disk_usage():
#         disk = psutil.disk_usage('/')
#         return f"{disk.used / (1024 ** 3):.2f} GB"

#     @staticmethod
#     def get_uptime():
#         boot_time = datetime.fromtimestamp(psutil.boot_time())
#         uptime = datetime.now() - boot_time
#         hours, remainder = divmod(uptime.total_seconds(), 3600)
#         minutes, _ = divmod(remainder, 60)
#         return f"{int(hours)}h {int(minutes)}m"

#     @staticmethod
#     def get_bandwidth():
#         bandwidth = psutil.net_io_counters()
#         return f"{bandwidth.bytes_sent / (1024 ** 2):.2f} MB sent"

#     @staticmethod
#     def get_live_metrics():
#         return [
#             {
#                 "title": "CPU",
#                 "value": f"{SystemMetrics.get_cpu_usage()}% usage",
#                 "icon": "Cpu",
#             },
#             {
#                 "title": "RAM",
#                 "value": f"{SystemMetrics.get_memory_usage()} used",
#                 "icon": "MemoryStick",
#             },
#             {
#                 "title": "Disk",
#                 "value": f"{SystemMetrics.get_disk_usage()} used",
#                 "icon": "HardDrive",
#             },
#             {
#                 "title": "Uptime",
#                 "value": f"{SystemMetrics.get_uptime()}",
#                 "icon": "Server",
#             },
#             {
#                 "title": "Bandwidth",
#                 "value": f"{SystemMetrics.get_bandwidth()}",
#                 "icon": "Network",
#             },
#         ]

#     @staticmethod
#     def generate_chart_data():
#         labels = [(datetime.now().replace(microsecond=0) - timedelta(seconds=i * 10)).strftime("%H:%M:%S") for i in range(5)]
#         cpu_data = [psutil.cpu_percent(interval=0.1) for _ in range(5)]
#         return {
#             "labels": labels[::-1],
#             "datasets": [
#                 {
#                     "label": "CPU Usage",
#                     "data": cpu_data,
#                     "backgroundColor": "rgba(75, 192, 192, 0.2)",
#                     "borderColor": "rgb(75, 192, 192)",
#                     "borderWidth": 2,
#                 }
#             ],
#         }

#     @staticmethod
#     def get_historical_data():
#         now = datetime.now()
#         history = []
#         for i in range(3):
#             history.append({
#                 "date": (now - timedelta(days=i)).strftime("%Y-%m-%d"),
#                 "cpu": f"{psutil.cpu_percent(interval=0.1)}%",
#                 "memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
#                 "bandwidth": f"{psutil.net_io_counters().bytes_sent / (1024 ** 2):.2f} MB sent",
#             })
#         return history

class SystemMetrics:
    """
    Helper class to encapsulate system metric fetching logic.
    """

    @staticmethod
    def get_cpu_usage():
        return psutil.cpu_percent(interval=0.1)

    @staticmethod
    def get_memory_usage():
        memory = psutil.virtual_memory()
        return f"{memory.used / (1024 ** 3):.2f} GB"

    @staticmethod
    def get_disk_usage():
        disk = psutil.disk_usage('/')
        return {
            "used": f"{disk.used / (1024 ** 3):.2f} GB",
            "free": f"{disk.free / (1024 ** 3):.2f} GB",
            "percent": f"{disk.percent}%",
        }

    @staticmethod
    def get_uptime():
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.now() - boot_time
        hours, remainder = divmod(uptime.total_seconds(), 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m"

    @staticmethod
    def get_bandwidth():
        bandwidth = psutil.net_io_counters()
        return {
            "sent": f"{bandwidth.bytes_sent / (1024 ** 2):.2f} MB",
            "recv": f"{bandwidth.bytes_recv / (1024 ** 2):.2f} MB",
        }

    @staticmethod
    def get_cost_distribution():
        # Mocking cost distribution for the demo
        return {
            "storage": 40,
            "compute": 35,
            "bandwidth": 25,
        }
    
    @staticmethod
    def generate_chart_data():
        labels = [(datetime.now().replace(microsecond=0) - timedelta(seconds=i * 10)).strftime("%H:%M:%S") for i in range(5)]
        cpu_data = [psutil.cpu_percent(interval=0.1) for _ in range(5)]
        return {
            "labels": labels[::-1],
            "datasets": [
                {
                    "label": "CPU Usage",
                    "data": cpu_data,
                    "backgroundColor": "rgba(75, 192, 192, 0.2)",
                    "borderColor": "rgb(75, 192, 192)",
                    "borderWidth": 2,
                }
            ],
        }
    @staticmethod
    def get_databases():
        # This is a placeholder; replace it with real logic based on your system
        # E.g., fetching databases, active connections, etc.
        return {"total": 5, "active": 3}

    @staticmethod
    def get_instances():
        # Example placeholder, replace with actual instances logic
        return {"running": 10, "stopped": 2}

    @staticmethod
    def get_firewall_status():
        # Placeholder logic, adapt to your firewall setup
        return {"status": "active", "rules": 25}

    @staticmethod
    def get_users():
        users = psutil.users()
        return {
            "total": len(users),
            "active": len(users)  # As all users in the list can be considered "active"
        }
    
    @staticmethod
    def get_live_metrics():
        return {
            "cpu": f"{SystemMetrics.get_cpu_usage()}%",
            "memory": SystemMetrics.get_memory_usage(),
            "disk": SystemMetrics.get_disk_usage(),
            "uptime": SystemMetrics.get_uptime(),
            "bandwidth": SystemMetrics.get_bandwidth(),
            "cost_distribution": SystemMetrics.get_cost_distribution(),
            "databases": SystemMetrics.get_databases()['total'],
            "instances": SystemMetrics.get_instances()['running'],
            "firewall": SystemMetrics.get_firewall_status()['status'],
            "users": SystemMetrics.get_users()['total']
        }

    # @staticmethod
    # def get_live_metrics():
    #     return [
    #         {
    #             "title": "CPU",
    #             "value": f"{SystemMetrics.get_cpu_usage()}% usage",
    #             "icon": "Cpu",
    #         },
    #         {
    #             "title": "RAM",
    #             "value": f"{SystemMetrics.get_memory_usage()} used",
    #             "icon": "MemoryStick",
    #         },
    #         {
    #             "title": "Disk",
    #             "value": f"{SystemMetrics.get_disk_usage()} used",
    #             "icon": "HardDrive",
    #         },
    #         {
    #             "title": "Uptime",
    #             "value": f"{SystemMetrics.get_uptime()}",
    #             "icon": "Server",
    #         },
    #         {
    #             "title": "Bandwidth",
    #             "value": f"{SystemMetrics.get_bandwidth()}",
    #             "icon": "Network",
    #         },
    #         {
    #             "title": "Databases",
    #             "value": f"{SystemMetrics.get_databases()['total']} databases",
    #             "icon": "Database",
    #         },
    #         {
    #             "title": "Instances",
    #             "value": f"{SystemMetrics.get_instances()['running']} running instances",
    #             "icon": "Server",
    #         },
    #         {
    #             "title": "Firewall",
    #             "value": f"Status: {SystemMetrics.get_firewall_status()['status']} | Rules: {SystemMetrics.get_firewall_status()['rules']}",
    #             "icon": "Shield",
    #         },
    #         {
    #             "title": "Users",
    #             "value": f"{SystemMetrics.get_users()['total']} total users",
    #             "icon": "Users",
    #         },
    #     ]

    @staticmethod
    def get_historical_data():
        now = datetime.now()
        history = []
        for i in range(3):
            history.append({
                "date": (now - timedelta(days=i)).strftime("%Y-%m-%d"),
                "cpu": f"{psutil.cpu_percent(interval=0.1)}%",
                "memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
                "bandwidth": f"{psutil.net_io_counters().bytes_sent / (1024 ** 2):.2f} MB sent",
            })
        return history


class LiveMetricsView(APIView):
    """
    API Endpoint for live system metrics.
    """
    def get(self, request):
        data = SystemMetrics.get_live_metrics()
        return Response(data)


class ChartDataView(APIView):
    """
    API Endpoint for chart data (e.g., CPU usage trends).
    """
    def get(self, request):
        data = SystemMetrics.generate_chart_data()
        return JsonResponse(data)


class HistoryDataView(APIView):
    """
    API Endpoint for historical system data.
    """
    def get(self, request):
        data = SystemMetrics.get_historical_data()
        return JsonResponse({"history": data})
