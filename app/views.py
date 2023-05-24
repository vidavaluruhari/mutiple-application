from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_string(request):
    return HttpResponse('<marquee>this is app view functionof string responce</marqee>')

def app_html(request):
    return render(request,'hari.html')