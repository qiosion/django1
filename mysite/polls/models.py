from django.db import models

class Book(models.Model):
    # bookid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=40, null=True, verbose_name='책이름')
    publisher = models.CharField(max_length=40, null=True, verbose_name='출판사')
    price = models.IntegerField(null=True, verbose_name='가격')
    stock = models.IntegerField(null=True, verbose_name='재고')

    # class Meta:
    #     db_table = 'book'

class Customer(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='이름')
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
