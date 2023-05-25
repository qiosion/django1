from django.db import models

class Book(models.Model):
    # bookid = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=40, null=True)
    publisher = models.CharField(max_length=40, null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)

    # class Meta:
    #     db_table = 'book'
