from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'), #доменсайта, + префикс noticeapp
    path('fullnotice/', fullNotice, name='fullnotice')
]

