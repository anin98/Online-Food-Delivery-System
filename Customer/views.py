import json
from django.shortcuts import render, redirect
from django.views import View
from .models import MenuItem, Category, OrderModel
from django.utils.timezone import datetime
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class Index(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'Customer/index.html')


class Menu(View) :
    def get(self, request, *args, **kwargs) :
        # get every item from each category
        appetizer = MenuItem.objects.filter(category__name__contains='Appetizer')
        mains = MenuItem.objects.filter(category__name__contains='Mains')
        dessert = MenuItem.objects.filter(category__name__contains='Dessert')
        beverage = MenuItem.objects.filter(category__name__contains='Beverage')

        # pass into context
        context = {
            'appetizer' : appetizer,
            'mains' : mains,
            'dessert' : dessert,
            'beverage' : beverage,
        }

        # render the template
        return render(request, 'Customer/menu.html', context)


class About(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'Customer/about.html')


class SignUp(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'account/signup.html')


class Payment(View) :
    def get(self, request, *args, **kwargs) :
        return render(request, 'Customer/payment.html')


class Order(View) :
    def get(self, request, *args, **kwargs) :
        # get every item from each category
        appetizer = MenuItem.objects.filter(category__name__contains='Appetizer')
        mains = MenuItem.objects.filter(category__name__contains='Mains')
        dessert = MenuItem.objects.filter(category__name__contains='Dessert')
        beverage = MenuItem.objects.filter(category__name__contains='Beverage')

        # pass into context
        context = {
            'appetizer' : appetizer,
            'mains' : mains,
            'dessert' : dessert,
            'beverage' : beverage,
        }

        # render the template
        return render(request, 'Customer/order.html', context)

    def post(self, request, *args, **kwargs) :
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        pay = request.POST.get('payment')
        delivery = False
        order_items = {
            'items' : []
        }

        items = request.POST.getlist('items[]')

        for item in items :
            menu_item = MenuItem.objects.get(pk=int(item))
            item_data = {
                'id' : menu_item.pk,
                'name' : menu_item.name,
                'price' : menu_item.price
            }

            order_items['items'].append(item_data)

            global price
            price = 0

            item_ids = []

        for item in order_items['items'] :
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(name=name, price=0, address=address, email=email, contact=contact,
                                          payment=pay, delivered=delivery)
        order.items.add(*item_ids)

        context = {
            'items' : order_items['items'],
            'price' : price
        }

        return render(request, 'Customer/order_confirmation.html', context)


class OrderConfirmation(View) :
    def get(self, request, pk) :
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk' : order.pk,
            'items' : order.items,
            'price' : order.price,
        }

    def post(self, request, pk, *args, **kwargs) :
        data = json.loads(request.body)

        if data['isPaid'] :
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('order_pay_confirmation')

    def post(self, request, pk, *args, **kwargs) :
        data = json.loads(request.body)

        if data['isPaid'] :
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('index')


class Dashboard(View) :
    def get(self, request, *args, **kwargs) :
        order = OrderModel.objects.all()
        total_revenue = 0

        # pass total number of orders and total revenue into template
        context = {
            'order' : order,
        }

        return render(request, 'Customer/dashboard.html', context)


class Delivery(View) :
    def post(self, request, *args, **kwargs) :
        pk = request.POST.get('pk')
        delivered = request.POST.get('delivered')
        order = OrderModel.objects.get(pk=pk)
        order.delivered = delivered
        order.save()
        return render(request, 'Customer/delivery.html')

    def get(self, request, *args, **kwargs) :
        order = OrderModel.objects.all()
        total_revenue = 0

        # pass total number of orders and total revenue into template
        context = {
            'order' : order,
        }

        return render(request, 'Customer/delivery.html', context)


class Authorize(View) :

    def get(self, request, *args, **kwargs) :

        if request.user.is_superuser :
            order = OrderModel.objects.all()
            context = {
                'order' : order,
            }
            return render(request, 'Customer/dashboard.html', context)

        elif request.user.is_staff :
            order = OrderModel.objects.all()
            context = {
                'order' : order,
            }

            return render(request, 'Customer/delivery.html', context)




        else :
            order = OrderModel.objects.all()
            context = {
                'order' : order,

            }
            return render(request, 'Customer/index.html', context)

    def post(self, request, *args, **kwargs) :
        pk = request.POST.get('pk')
        delivered = request.POST.get('delivered')
        order = OrderModel.objects.get(pk=pk)
        order.delivered = delivered
        order.save()
        return render(request, 'Customer/index.html')
