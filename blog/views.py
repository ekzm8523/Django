from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView,\
                                       DayArchiveView, TodayArchiveView
from django.views.generic import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from blog.models import Post
from django.conf import settings
# Create your views here.


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # default 는 blog/post_list.html 이다.
    context_object_name = 'posts'   # 템플릿 파일로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명을 'posts'로 지정
    paginate_by = 2


class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context


class PostAV(ArchiveIndexView):
    model = Post
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


class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    model = Post
    template_name = 'taggit/taggit_post_list.html'

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context


class SearchFormView(FormView):
    """
    FormView 제네릭 뷰는 GET 요청인 경우 폼을 화면에 보여주고 사용자의 입력을 기다린다.
    사용자가 폼에 데이터를 입력한 후 제출하면 이는 POST 요청으로 접수되며 FormView 클래스는 데이터에 대한 유효성 검사를 한다.
    데이터가 유효하지 않으면 form_valid() 함수를 실행한 후에 적절한 URL로 리다이렉트 시키는 기능을 가진다.
    """
    from_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']   # search_word는 froms.PostSearchForm 클래스에서 정의한 필드네임

        post_list = Post.objects.filter(
            Q(title__icontains=searchWord) |    # icontains -> 대소문자 구별 X
            Q(description__icontains=searchWord) |
            Q(content__icontains=searchWord)
        ).distinct()    # 중복 제거
        # Post 테이블의 모든 레코드에 대해 title, description, content 컬럼에 searchWord가 포함된 레코드를 대소문자 구별 없이 검색하고
        # 서로 다른 레코드들만 리스트로 만들어서 post_list에 저장한다.

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        # render()는 템플릿 파일과 컨텍스트 변수를 처리해 최종적으로 HttpResponse 객체를 반환한다.
        # form_valid() 메서드는 보통 리다이렉트 처리를 위해 HttpResponseRedirect 객체를 반환한다.
        # 여기서는 form_valid를 재정의 하여 render 함수를 사용함으로써 HttpResponse 객체를 반환한다. 즉 redirect 처리가 되지 않는다.
        return render(self.request, self.template_name, context)