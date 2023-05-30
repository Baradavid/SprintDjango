from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Users, PerevalAdded, Coords, PerevalImages


class PerevalTests(APITestCase):
    def setUp(self):
        self.url_post = reverse('submitData')
        self.url_post = reverse('getData', kwargs={'pk': 2})
        self.user = Users.objects.create(first_name='TestUser', last_name='Test',
                                         password='testpass', email='Testemail')
        self.coord = Coords.objects.create(latitude=1.0, longitude=3.0, height=2)
        self.img = PerevalImages.objects.create(image='Testimage.jpg',
                                                image_name='Testimage')
        self.valid_payload = {
            'user': self.user.pk,
            'beauty_title': 'Test Beauty Title',
            'title': 'Test Title',
            'other_titles': 'Test Other Titles',
            'connect': 'Test Connect',
            'winter_level': 'Test Winter Level',
            'spring_level': 'Test Spring Level',
            'summer_level': 'Test Summer Level',
            'autumn_level': 'Test Autumn Level',
            'coord_id': self.coord.pk,
            'images': [self.img.pk],
            'status': 'new'
        }
        self.invalid_payload = {
            'user': '',
            'beauty_title': '',
            'title': '',
            'other_titles': '',
            'connect': '',
            'winter_level': '',
            'summer_level': '',
            'autumn_level': '',
            'spring_level': '',
            'coord_id': '',
            'images': [],
            'status': ''
        }




