from rest_framework import serializers
from .models import Room, Resident, RoomBooking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'


class RoomBookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    resident = ResidentSerializer()

    class Meta:
        model = RoomBooking
        fields = '__all__'