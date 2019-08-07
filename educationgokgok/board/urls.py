from django.urls import path
from . import views

#미디어파일 업로드를 위해 추가_현지원
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
    # path('detail/<int:post_id>', views.detail, name='detail'),
    path('main/', views.board_main, name='board_main'),
    path('major/', views.board_major, name='board_major'),
    path('local/', views.board_local, name='board_local'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #미디어 파일 업로드
