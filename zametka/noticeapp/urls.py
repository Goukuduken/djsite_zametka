from django.urls import path

from .views import *

urlpatterns = [
    path('', NoticeHome.as_view(), name='home'), #доменсайта, + префикс noticeapp
    path('addnotice/', add_notice, name='addnotice'),
    path('fullnotice/', full_notice, name='fullnotice')

]

