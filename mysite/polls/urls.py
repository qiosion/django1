from django.urls import path
from . import views

# URL 연결 설정
urlpatterns = [
    path("", views.index, name="index"),
    path("booklist", views.booklist, name="booklist"),
    path("bookview", views.bookview, name="bookview"),
    # path("postbook", views.postbook, name="postbook"),
    # path("book", views.book, name="book"),
]