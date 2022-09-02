from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .forms import *
from .models import *
# Create your views here.

add_notice_btn = {'url_name': 'add_notice'}

def index(request):
    notice_card_information = Notice.objects.all()
    return render(request, 'notice/index.html', {'notice_card_information': notice_card_information})

def fullNotice(request):
    if request.method == 'POST':
        form = AddNotice(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddNotice()
    return render(request, 'notice/fullnotice.html', {'form': form})

#exceptions
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")