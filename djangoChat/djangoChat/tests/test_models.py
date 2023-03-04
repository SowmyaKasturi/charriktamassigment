from django.test import TestCase
from room.models import Room

class AnimalTestCase(TestCase):
    def setUp(self):
        Room.objects.create(name="Afterhours", slug="fun")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        room = Room.objects.get(name="Afterhours")
        self.assertEqual(room.slug, 'fun')