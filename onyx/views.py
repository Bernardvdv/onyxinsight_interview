from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Data, Sensor
from .serializers import DataSerializer, SensorSerializer


class SensorListApiView(APIView):
    def get(self, request, id=None):
        """
        List all the sensor items for given requested sensor or all if no sensor
        is provided
        :param request: A request object
        :return:Rest framework response
        """
        if id:
            queryset = Sensor.objects.get(id=id)
            serialized_data = SensorSerializer(queryset)
            return Response({"status": "success", "data": serialized_data.data}, status=status.HTTP_200_OK)

        queryset = Sensor.objects.all()
        serializer = SensorSerializer(queryset, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add new sensors to the sensor model
        :param request: A request object
        :return:Rest framework response
        """
        data = {
            'name': request.data.get('name'),
            'unit': request.data.get('unit'),
        }
        serialized_data = SensorSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class DataListApiView(APIView):
    # Allowed HTTP methods
    http_method_names = ['get', 'post', 'patch']

    def get(self, request):
        """
        List all the data items for given requested sensor or all if no sensor
        is provided
        :param request: A request object
        :return:Rest framework response
        """
        if request.GET.get('sensor'):
            sensor = request.GET['sensor']
            queryset = Data.objects.filter(sensor=sensor)
            serialized_data = DataSerializer(queryset, many=True)
            return Response({"status": "success", "data": serialized_data.data}, status=status.HTTP_200_OK)

        queryset = Data.objects.all()
        serializer = DataSerializer(queryset, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add sensor data to data model
        :param request: A request object
        :return:Rest framework response
        """
        data = {
            "sensor": request.data.get('sensor'),
            "value": request.data.get('value')
        }

        serialized_data = DataSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        """
        Allow patching of sensor data to data model
        :param request: A request object
        :param id: Sensor ID which should be patched
        :return:Rest framework response
        """
        sensor = Data.objects.get(id=id)
        serialized_data = DataSerializer(sensor, data=request.data, partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({"status": "success", "data": serialized_data.data})
        return Response({"status": "error", "data": serialized_data.errors})
