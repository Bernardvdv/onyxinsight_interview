from django.urls import path

from .views import (
    DataListApiView,
    SensorListApiView,
)


urlpatterns = [
    path("sensor/", SensorListApiView.as_view()),
    path('sensor/<int:id>', SensorListApiView.as_view()),
    path("data/", DataListApiView.as_view()),
    path("data/<int:id>", DataListApiView.as_view()),
]
