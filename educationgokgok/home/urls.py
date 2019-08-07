from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('menti_info/', views.menti_info, name='menti_info'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
