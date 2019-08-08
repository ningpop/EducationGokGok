from django.shortcuts import render
# from django.shortcuts import get_object_or_404, redirect
# from .models import AAA (AAA: board앱 내 models.py의 class명)
# from django.utils import timezone
# from django.core.paginator import Paginator

# Create your views here.
'''
* 키워드 단어 정리 *
board : 강의 글들의 게시판
post : 하나의 강의 글
post_detail : 각각 강의 글의 detail
post_list : 강의 글들의 게시판보다는 작은 개념, 글 들의 목록을 뜻함
'''
def new(request):
    return render(request, 'new.html')

'''
-> 글쓰기 후 form action으로 실행될 create 함수
def create(request):
    post = AAA()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/' + str(post.id))
'''

def detail(request):
    return render(request, 'detail.html')
'''
-> 추후 대체될 detail 함수
def detail(request, post_id):
    post_detail = get_object_or_404(AAA, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})
'''


def board_main(request):
    '''
    post_list = AAA.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})
    '''
    return render(request, 'board_main.html')

'''
* 전공 목록 *
IT 음악 미술 체육 etc
'''
def board_major(request):
    '''
    major_post_list = AAA.objects.order_by('major', '-pub_date') # major: 필드명
    paginator = Paginator(major_post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})
    '''
    return render(request, 'board_major.html')

'''
* 지역 목록 *
특별시: 서울(1)
광역시: 부산(2) 대구(3) 인천(4) 광주(5) 대전(6) 울산(7)
특별자치시: 세종(8)
도: 경기(10) 강원(11) 충청(12) 전라(13) 경상(14) 제주(15)
'''
def board_local(request):
    '''
    local_post_list = AAA.objects.order_by('area', -pub_date') # area: 필드명
    paginator = Paginator(local_post_list, 10)
    page = request.GET.get('page')
    board = paginator.get_page(page)
    return render(request, 'board_main.html', {'board':board})
    '''
    return render(request, 'board_local.html')