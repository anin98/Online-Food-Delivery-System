from django.shortcuts import render, redirect
from django.views import View
from django.test import TestCase
from Customer.models import MenuItem, Category, OrderModel
from datetime import datetime

class TestCategory (TestCase):
    def test_should_create_category(self):
         cname= Category.objects.create(name='Sides')
         cname.save()
         self.assertEqual(str(cname),'Sides')

class TestOrder (TestCase):
    def test_should_create_price(self):
        price=OrderModel.objects.create()
        price= OrderModel.objects.create(price=220.00)
        price.save()
        self.assertEqual(price, price)
    def test_should_create_name(self):
        name=OrderModel.objects.create()
        name= OrderModel.objects.create(name="Anin")
        name.save()
        self.assertEqual(name, name)

    def test_should_create_price(self):
        address=OrderModel.objects.create()
        address= OrderModel.objects.create(address="Kakrail")
        address.save()
        self.assertEqual(address, address)

    def test_should_create_email(self):
        email=OrderModel.objects.create()
        email= OrderModel.objects.create(email="anin@gmail.com")
        email.save()
        self.assertEqual(email, email)

    def test_should_create_contact(self):
        contact=OrderModel.objects.create()
        var=0o1234567
        contact= OrderModel.objects.create(contact=var)
        contact.save()
        self.assertEqual(contact, contact)
