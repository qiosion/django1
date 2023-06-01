from django.contrib import admin
from .models import Book, Customer


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'bookname']
admin.site.register(Book, BookAdmin) # book 모델을 bookAdmin이라는 모습으로 보여줄거다

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
admin.site.register(Customer, CustomerAdmin)
