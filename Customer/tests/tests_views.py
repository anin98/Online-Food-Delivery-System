from django.test import TestCase
from django.test import Client
from django.urls import reverse
class TestViews(TestCase):
    def post_case(self):
        c= Client()
        response= self.client.post('/order-confirmation')
        self.assertEqual(response.status,200)
