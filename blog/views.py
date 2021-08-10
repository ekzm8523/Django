from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView,\
                                       DayArchiveView, TodayArchiveView
from blog.models import Post
# Create your views here.


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # default 는 blog/post_list.html 이다.
    context_object_name = 'posts'   # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 'posts'로 지정
    paginate_by = 2


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    # template_name = 'blog/post_archive.html'
    date_field = 'modify_dt'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True     # 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨준다. 즉 템플릿 파일에서 object_list 변수를 사용 가


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'


class PostTAV(TodayArchiveView):
    model = Post
    # template_name = 'blog/post_archive_day.html'
    date_field = 'modify_dt'

