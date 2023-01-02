from django.urls import path, include
from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('platform', views.platform, name='platform'),
    path('fund_account', views.fund_account, name='fund_account'),
    path('withdraw_account', views.withdraw_account, name='withdraw_account'),
    path('trade_history', views.trade_history, name='trade_history'),
    path('profile', views.profile, name='profile'),
    path('bitcoin', views.bitcoin, name='bitcoin'),
    path('ethereum', views.ethereum, name='ethereum'),
    path('usdt', views.usdt, name='usdt'),
]