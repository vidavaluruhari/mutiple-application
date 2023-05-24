from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_string(request):
    return HttpResponse('<marquee>this is app2 string response</marqee>')

def app2_html(request):
    return render(request,'hari2.html')
