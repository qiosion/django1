from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple
from .models import Book

def index(request):
    return HttpResponse("와 이거 좀 어렵다;")

# 데이터베이스 연동
def booklist(request):
    results = []
    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'polls/booklist.html', context)

# table 의 컬럼 이름을 이용해서 각 record를 dictionary로 변환
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def book(request):
    results = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book")
        queryset = namedtuplefetchall(cursor)

    for row in queryset:
        results.append(f'{row.bookname}')
        results.append('<br>')

    return HttpResponse(results)

def bookview(request):
    bookid = request.GET.get('id', None) # 요청 서버에서 책 번호 받아옴
    book = Book.objects.get(bookid=bookid)
    context = {'book': book}
    # return HttpResponse(book)
    # return HttpResponse(book.bookname) # 책 이름만 가져와봄
    return render(request, 'polls/bookview.html', context)