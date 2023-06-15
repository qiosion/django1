from django.urls import path
from . import views

# URL 연결 설정
urlpatterns = [
    path("", views.index, name="index"),

    # generic view
    path("book/list", views.BookListView.as_view(), name="book_list"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book_view"),
    path("book/create", views.BookCreateView.as_view(), name="book_create"),
    path("book/<int:pk>/edit", views.BookUpdateView.as_view(), name="book_update"),
    path("book/<int:pk>/delete", views.BookDeleteView.as_view(), name="book_delete"),

    path("booklist", views.booklist, name="booklist"),
    path("bookview/<int:id>", views.bookview, name="bookview"),
    path("postbook", views.postbook, name="postbook"),
    path("createbook", views.createbook, name="createbook"),
    path("editbook/<int:id>", views.editbook, name="editbook"),
    path("deletebook/<int:id>", views.deletebook, name="deletebook"),
    path("book", views.book, name="book"),

    path("customerlist", views.customerlist, name="customerlist"),
    path("customerview/<int:id>", views.customerview, name="customerview"),
    path("createcustomer", views.createcustomer, name="createcustomer"),
    path("editcustomer/<int:id>", views.editcustomer, name="editcustomer"),
    path("deletecustomer/<int:id>", views.deletecustomer, name="deletecustomer"),
]