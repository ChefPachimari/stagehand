from django.test import TestCase, Client
from django.urls import reverse

from toolbox.models import Numbers

class DifferenceView(TestCase):
    def setUp(self):
        self.client = Client()
        Numbers.objects.create(number=1, request_ct=0)
        Numbers.objects.create(number=2, request_ct=0)
        Numbers.objects.create(number=3, request_ct=0)
        Numbers.objects.create(number=4, request_ct=0)
        Numbers.objects.create(number=5, request_ct=0)
        Numbers.objects.create(number=6, request_ct=0)
        Numbers.objects.create(number=7, request_ct=0)
        Numbers.objects.create(number=8, request_ct=0)
        Numbers.objects.create(number=9, request_ct=0)
        Numbers.objects.create(number=10, request_ct=0)

    def test_differences(self):
        response = self.client.get(reverse('difference'), {'number': 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['value'], 2640)
        self.assertEqual(response.data['number'], 10)
        self.assertEqual(response.data['occurences'], 0)
        self.assertEqual(response.data['has_triplet'], [])

    def test_occurence_incrementing(self):
        response = self.client.get(reverse('difference'), {'number': 10})
        response = self.client.get(reverse('difference'), {'number': 10})
        self.assertEqual(response.data['occurences'], 1)

    def test_last_timestamp(self):
        # create double requests
        response = self.client.get(reverse('difference'), {'number': 10})
        response = self.client.get(reverse('difference'), {'number': 10})
        self.assertIsNotNone(response.data['last_datetime'])

    def test_triplet(self):
        response = self.client.get(reverse('difference'), {'number': 60})
        self.assertEqual(response.data['has_triplet'], [3,4,5])
        response = self.client.get(reverse('difference'), {'number': 61})
        self.assertEqual(response.data['has_triplet'], [])

    def test_json_structure(self):
        response = self.client.get(reverse('difference'), {'number': 10})
        self.assertIn('datetime', response.data)
        self.assertIn('value', response.data)
        self.assertIn('number', response.data)
        self.assertIn('occurences', response.data)
        self.assertIn('last_datetime', response.data)
        self.assertIn('has_triplet', response.data)