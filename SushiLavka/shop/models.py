from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    svg = models.TextField()
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list', args=[self.slug])



class Types(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ManyToManyField(Category, related_name='types')

    class Meta:
        verbose_name = 'types'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    characteristics = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    types = models.ManyToManyField(Types, related_name='type_products')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.IntegerField()
    weight = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


    