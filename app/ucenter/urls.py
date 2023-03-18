from django.urls import path, include
from . import views


app_name = 'ucenter'
urlpatterns = [
    path('1/', views.WithdrawView1.as_view(), name='withdraw1'),
    path('2/', views.WithdrawView2.as_view(), name='withdraw2'),
    path('3/', views.WithdrawView3.as_view(), name='withdraw3'),
    path('4/', views.WithdrawView3.as_view(), name='withdraw4'),
]
