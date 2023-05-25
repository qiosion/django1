from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple

from .forms import BookForm
from .models import Book

# 인덱스페이지
def index(request):
    context = { 'app_name': 'polls' }
    # return HttpResponse("polls 의 index 페이지")
    return render(
        request,
        'polls/index.html',
        context
    )

# 데이터베이스 연동
# 도서목록
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

# 얘는 진짜그냥 도서 제목만 보는거..
def book(request):
    results = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM polls_book") # 테이블명 바껴서 수정해줌
        queryset = namedtuplefetchall(cursor)

    for row in queryset:
        results.append(f'{row.bookname}')
        results.append('<br>')

    return HttpResponse(results)

# 도서 1개 조회
def bookview(request, id):
    # bookid = request.GET.get('id', None) # 요청 서버에서 책 번호 받아옴
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'polls/bookview.html', context)

# 도서 등록
def postbook(request):
    context = {}
    if request.method == 'POST':
        result = False
        try:
            bookname = request.POST.get('bookname', '')
            publisher = request.POST.get('publisher', '')
            price = request.POST.get('price')
            book = Book(bookname=bookname, publisher=publisher, price=price)
            book.save()
            result = True
        except:
            result = False
        context = {'result': result}
        return render(
            request,
            'polls/postresult.html',
            context
        )
    return render(
        request,
        'polls/postbook.html',
        context
    )

# 장고 Form 사용
# 도서 create, update, delete
def createbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    form = BookForm()
    return render(
        request,
        'polls/createbook.html',
        {'form': form}
    )

def editbook(request, id):
    return HttpResponse("createbook")

def deletebook(request, id):
    return HttpResponse("createbook")
