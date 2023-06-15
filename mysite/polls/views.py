import traceback

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from collections import namedtuple

from django.urls import reverse_lazy
from django.views import generic

from .forms import BookForm, CustomerForm
from .models import Book, Customer


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
# generic
class BookListView(generic.ListView):
    model = Book
    template_name = "polls/book_list.html"
    context_object_name = "books"

class BookDetailView(generic.DetailView):
    model = Book
    template_name = "polls/book_view.html"
    context_object_name = "book"

class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "polls/book_create.html"
    success_url = reverse_lazy("book_list")

class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "polls/book_update.html"
    success_url = reverse_lazy("book_list")

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "polls/book_delete.html"
    success_url = reverse_lazy("book_list")
    context_object_name = "book"




# 도서목록
def booklist(request):
    results = []
    """
    with connection.cursor() as cursor: # 데이터베이스 연결 및 커서 사용을 관리
        cursor.execute("SELECT * FROM book") # sql문 실행
        queryset = namedtuplefetchall(cursor)
    """

    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'polls/booklist.html', context)

# table 의 컬럼 이름을 이용해서 각 record를 dictionary로 변환
def namedtuplefetchall(cursor): # 데이터베이스에서 검색된 결과를 namedtuple 형태로 변환하여 반환하는 함수
    desc = cursor.description # 각 컬럼의 정보를 담은 튜플들의 리스트

    nt_result = namedtuple("Result", [col[0] for col in desc])
    # Result라는 이름의 namedtuple을 생성
    # 컬럼 정보에서 컬럼명만 추출하여 필드명으로 사용

    return [nt_result(*row) for row in cursor.fetchall()]
# nt_result(*row) : row에서 추출한 각 컬럼 값을 namedtuple의 필드에 매핑하여 객체를 생성

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
    if request.method == 'POST':
        result = '실패'
        book = Book.objects.get(id=id)
        form = BookForm(request.POST, instance=book)
        try:
            if form.is_valid():
                form.save()
                result = '성공'
            else:
                result = form.errors
        except:
            result = traceback.format_exc()
        context = {'result': result}
        return render(
            request,
            'polls/postresult.html',
            context
        )
    else:
        book = Book.objects.get(id=id)
        form = BookForm(instance=book)
        return render(
            request,
            'polls/editbook.html',
            {'form': form}
        )

def deletebook(request, id):
    if request.method == 'POST':
        result = '실패'
        try:
            book = Book.objects.get(id=id)
            book.delete()
            result = '성공'
        except:
            result = traceback.format_exc()
        context = {'result': result}
        return render(request,
                      'polls/postresult.html',
                      context)
    else:
        book = Book.objects.get(id=id)
        return render(request,
                      'polls/deletebook.html',
                      {'book': book})

# 고객목록
def customerlist(request):
    results = []
    queryset = Customer.objects.all()
    context = {'customers': queryset}
    return render(request, 'polls/customerlist.html', context)

# 고객조회
def customerview(request, id):
    customer = Customer.objects.get(id=id)
    context = {'customer': customer}
    return render(request, 'polls/customerview.html', context)

# 장고 Form 사용
# 고객 create, update, delete
def createcustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customerlist')
    form = CustomerForm()
    return render(
        request,
        'polls/createcustomer.html',
        {'form': form}
    )

def editcustomer(request, id):
    if request.method == 'POST':
        result = '실패'
        customer = Customer.objects.get(id=id)
        form = CustomerForm(request.POST, instance=customer)
        try:
            if form.is_valid():
                form.save()
                result = '성공'
            else:
                result = form.errors
        except:
            result = traceback.format_exc()
        context = {'result': result}
        return render(
            request,
            'polls/customeresult.html',
            context
        )
    else:
        customer = Customer.objects.get(id=id)
        form = CustomerForm(instance=customer)
        return render(
            request,
            'polls/editcustomer.html',
            {'form': form}
        )

def deletecustomer(request, id):
    if request.method == 'POST':
        result = '실패'
        try:
            customer = Customer.objects.get(id=id)
            customer.delete()
            result = '성공'
        except:
            result = traceback.format_exc()
        context = {'result': result}
        return render(request,
                      'polls/customeresult.html',
                      context)
    else:
        customer = Customer.objects.get(id=id)
        return render(request,
                      'polls/deletecustomer.html',
                      {'customer': customer})