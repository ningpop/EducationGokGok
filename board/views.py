from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Mento
# from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mento

'''
* 키워드 단어 정리 *
board : 강의 글들의 게시판
post : 하나의 강의 글
post_detail : 각각 강의 글의 detail
post_list : 강의 글들의 게시판보다는 작은 개념, 글 들의 목록을 뜻함
'''
class MentoView(ListView):
    model = Mento
    #context_object_name =''
    template_name ="board_main.html"

class MentoLocalView(ListView):
    template_name ="board_local.html"
    model = Mento
    def get_queryset(self):
        return Mento.objects.order_by('area')
    #model = Mento
    #context_object_name =''
    

class MentoMajorView(ListView):
    template_name ="board_major.html"
    model = Mento
    def get_queryset(self):
        return Mento.objects.order_by('major')

class MentoCreate(CreateView):
    model = Mento
    fields = ['title', 'major', 'area', 'body', 'contact']
    success_url = reverse_lazy('board_main')
    template_name ="new.html"

class MentoDetail(DetailView):
    model = Mento
    template_name ="detail.html"

class MentoUpdate(UpdateView):
    model = Mento
    fields = ['title', 'major', 'area', 'body', 'contact']
    success_url = reverse_lazy('board_main')
    template_name ="create.html"
    
class MentoDelete(DeleteView):
    model = Mento
    success_url = reverse_lazy('board_main')
    template_name ="delete.html"

'''
def new(request):
    return render(request, 'new.html')



-> 글쓰기 후 form action으로 실행될 create 함수
def create(request):
    post = Mento()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.save()
    return redirect('/' + str(post.id))

def detail(request):
    return render(request, 'detail.html')

-> 추후 대체될 detail 함수
def detail(request, post_id):
    post_detail = get_object_or_404(Mento, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def board_main(request):
    post_list = Mento.objects.all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})

* 전공 목록 *
IT 음악 미술 체육 etc

def board_major(request):
    major_post_list = Mento.objects.order_by('major') # major: 필드명
    paginator = Paginator(major_post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})


* 지역 목록 *
특별시: 서울(1)
광역시: 부산(2) 대구(3) 인천(4) 광주(5) 대전(6) 울산(7)
특별자치시: 세종(8)
도: 경기(10) 강원(11) 충청(12) 전라(13) 경상(14) 제주(15)

def board_local(request):
    local_post_list = Mento.objects.order_by('area') # area: 필드명
    paginator = Paginator(local_post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})
'''