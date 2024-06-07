from rest_framework import viewsets
from .models import Room, Resident, RoomBooking
from .serializers import RoomSerializer, ResidentSerializer, RoomBookingSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer