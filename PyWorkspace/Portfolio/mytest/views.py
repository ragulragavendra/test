from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def htmlHello(requests):
 return render(requests,'index.html')

# Create your views here.
def hello(requests,username, age):
 return HttpResponse(f"Hello {username}, your age is {age}")

def old_url_redirect(requests):
 return redirect(reverse("mytest:new_url_name")) #mention app_name:name of the url path

def new_url(requests):
 return HttpResponse("You are in new Url")

