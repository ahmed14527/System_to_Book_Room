from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ResidentViewSet, RoomBookingViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'residents', ResidentViewSet)
router.register(r'bookings', RoomBookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]