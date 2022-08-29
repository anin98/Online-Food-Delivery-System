from django.db import models
global price

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50,blank=True)
    address = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=100,blank=True,null=True)
    payment = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)


    #def __str__(self):
        #return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
