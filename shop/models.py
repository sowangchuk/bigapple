from django.db import models
from django.urls import reverse
import datetime

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class landing1(models.Model):
    image=models.ImageField(upload_to='iamge', blank=False)
    title=models.TextField(max_length=100)
    info = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True,)
    def __str__(self):
     return f"{self.created.strftime('%d-%m-%Y')}"
     

class activelanding(models.Model):
    image=models.ImageField(upload_to='iamge', blank=False)
    title=models.TextField(max_length=100)
    info = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True,)
    def __str__(self):
     return f"{self.created.strftime('%d-%m-%Y')}"
   

class featureProduct(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

class address(models.Model):
    phone=models.IntegerField()
    location=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)

class service(models.Model):
    shipping = models.CharField(max_length=300)
    returns = models.CharField(max_length=300)
    support = models.CharField(max_length=300)
