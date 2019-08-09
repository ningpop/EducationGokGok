from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
    # path('detail/<int:post_id>', views.detail, name='detail'),
    path('main/', views.board_main, name='board_main'),
    path('major/', views.board_major, name='board_major'),
    path('local/', views.board_local, name='board_local'),
]
