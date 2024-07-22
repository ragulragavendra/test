from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import requests as req

def htmlHello(requests):
 return render(requests,'index.html')

# Create your views here.
def hello(requests,username, age):
 return HttpResponse(f"Hello {username}, your age is {age}")

def old_url_redirect(requests):
 return redirect(reverse("mytest:new_url_name")) #mention app_name:name of the url path

def new_url(requests):
 return HttpResponse("You are in new Url")

def proxy_view(request):
    target_url = 'https://django-nt56.onrender.com/mytest/newurl/'
    
    try:
        response = req.get(target_url)
        
        # Check the content type of the response
        content_type = response.headers.get('Content-Type')

        if 'application/json' in content_type:
            return JsonResponse(response.json(), safe=False)
        else:
            return HttpResponse(response.content, content_type=content_type)
    except req.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
