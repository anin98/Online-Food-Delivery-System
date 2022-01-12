from django.http import request
from django.shortcuts import render
from django.test import TestCase
import urllib.request

from django.urls import reverse, resolve
from django.views import View
from Customer.views import Index, About , Order, OrderConfirmation, Payment, Menu, Dashboard, SignUp, Authorize


class TestUrls(TestCase):
    def test_index_url_is_resolved(self):
      url = self.client.get('')
      self.assertEqual(url.status_code,200)


    def test_About_is_resolved(self):
      url = render(request, 'Customer/about.html')
      self.assertEqual(url.status_code,200)



    def test_menu_is_resolved(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code,200)


    def test_Order_is_resolved(self):
        url = self.client.get('/')
        self.assertEqual(url.status_code,200)



    def test_OrderConfirmation_is_resolved(self):
         url = self.client.get('/')
         self.assertEqual(url.status_code,200)


    def test_Payment_is_resolved(self):
         url = self.client.get('/')
         self.assertEqual(url.status_code,200)

    def test_Dashboard_is_resolved(self):
         url = self.client.get('/')
         self.assertEqual(url.status_code,200)

    def test_Signup_is_resolved(self):
         url = self.client.get('/')
         self.assertEqual(url.status_code,200)

    def test_Authorize_is_resolved(self):
         url = self.client.get('/')
         self.assertEqual(url.status_code,200)








