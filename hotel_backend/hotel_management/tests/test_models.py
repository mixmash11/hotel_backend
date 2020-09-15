import pytest

from ..models import Room

pytestmark = pytest.mark.django_db


def test___str__():
    room = Room.objects.create(room_number="1a", room_description="A comfy room")
    assert room.__str__() == "1a"
    assert str(room) == "1a"
