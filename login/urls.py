from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login),
    path('home/',views.home),
    path('history/',views.history),
    path('account/',views.account),
    path('recharge/',views.recharge)
]