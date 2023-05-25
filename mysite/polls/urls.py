from django.urls import path
from . import views

# URL 연결 설정
urlpatterns = [
    path("", views.index, name="index"),
    path("booklist", views.booklist, name="booklist"),
    path("bookview/<int:id>", views.bookview, name="bookview"),
    path("postbook", views.postbook, name="postbook"),
    path("createbook", views.createbook, name="createbook"),
    path("editbook/<int:id>", views.editbook, name="editbook"),
    path("deletebook/<int:id>", views.deletebook, name="deletebook"),
    path("book", views.book, name="book"),
]