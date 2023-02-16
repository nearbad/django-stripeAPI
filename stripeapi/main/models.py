from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена товара')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.IntegerField(verbose_name='Общая цена')
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Скидка')
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Налоги')


class Discount(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название скидки')
    amount = models.IntegerField()

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название налога')
    rate = models.FloatField()

    def __str__(self):
        return self.name
