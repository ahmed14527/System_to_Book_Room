from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(TimeStampModel):
    class RoomType(models.TextChoices):
        FOCUS = 'focus', 'FOCUS Room'
        TEAM = 'team', 'TEAM Room'
        CONFERENCE = 'conference', 'CONFERENCE Room'

    name = models.CharField(max_length=120, verbose_name=_("Name"))
    type = models.CharField(max_length=60, choices=RoomType.choices, default=RoomType.FOCUS, verbose_name=_("Type"))
    capacity = models.IntegerField(verbose_name=_("Capacity"))

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")

    def __str__(self):
        return self.name


class Resident(models.Model):
    name = models.CharField(max_length=120, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class RoomBooking(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name="room_bookings", null=True,
                                 blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room_bookings")
    start = models.DateTimeField()
    end = models.DateTimeField()
    booked = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Room Book")
        verbose_name_plural = _("Room Books")

        constraints = [
            models.CheckConstraint(
                check=~Q(start__gte=models.F('end')),
                name='start_before_end'
            ),
        ]

    def __str__(self):
        return self.room.name