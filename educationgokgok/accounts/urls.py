from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup_menti/', views.signup_menti, name='signup_menti'),
    path('signup_mento/', views.signup_mento, name='signup_mento'),
    path('login/', views.login, name='login'),
]