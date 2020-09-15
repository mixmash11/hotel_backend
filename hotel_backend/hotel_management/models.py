from django.db import models
from django_extensions.db.fields import AutoSlugField


class Room(models.Model):
    class RoomState(models.TextChoices):
        OPEN = "open", "Open"
        RESERVED = "reserved", "Reserved"
        OCCUPIED = "occupied", "Occupied"
        UNAVAILABLE = "unavailable", "Unavailable"
        OUT_OF_ORDER = "out of order", "Out of Order"

    room_number = models.CharField("Room Number", max_length=255, unique=True)
    slug = AutoSlugField("Room URL Slug", populate_from="room_number")
    room_description = models.TextField("Room Description", max_length=255)
    room_state = models.CharField(
        "Room Status", max_length=20, choices=RoomState.choices, default=RoomState.OPEN
    )

    def __str__(self):
        return self.room_number
