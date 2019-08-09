from django.urls import path
from . import views

#미디어파일 업로드를 위해 추가_현지원
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('major/', views.MentoMajorView.as_view(), name='board_major'),
    path('local/', views.MentoLocalView.as_view(), name='board_local'),
    path('', views.MentoView.as_view(), name='board_main'),
    path('new/', views.MentoCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.MentoDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.MentoUpdate.as_view(), name='change'),
    #path('delete/<int:pk>', views.MentoDelete.as_view(), name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #미디어 파일 업로드