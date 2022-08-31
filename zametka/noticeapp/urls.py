from django.urls import path

from .views import *

urlpatterns = [
    path('', index), #доменсайта, + префикс noticeapp
    path('opennotice/<int:notice_id>/', fullNotice)
]

