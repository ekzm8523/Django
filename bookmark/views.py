from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    """
    명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2가지 있다.
    1. 컨텍스트 변수로 object_list 를 사용한다.
    2. 템플릿 파일명을 모델명 소문자_list.html 형식의 이름으로 지정한다.
    """
    model = Bookmark


class BookmarkDV(DetailView):
    """
    명시적으로 지정하지 않아도 장고에서 디폴트로 알아서 지정해주는 속성이 2가지 있다.
    1. 컨텍스트 변수로 object 를 사용한다.
    2. 템플릿 파일명을 모델명 소문자_detail.html 형식의 이름으로 지정한다.
    """
    model = Bookmark
