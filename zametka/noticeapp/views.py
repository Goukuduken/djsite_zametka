from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    notice_card_inforamtion = Notice.objects.all()
    return render(request, 'notice/index.html', {'title_notice': notice_card_inforamtion[0],
                                                 'text_notice': notice_card_inforamtion[0]})

def fullNotice(request, notice_id):
    return HttpResponse(f"<h1>FULL NOTICE</h1><p>{notice_id}</p>")

#exceptions
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")