from django.urls import path
from . import views

app_name="mytest"

urlpatterns = [
    path('hello/<username>/<int:age>', views.hello, name="hello"),
    path("oldurl/",views.old_url_redirect, name="old_url_name"),
    path("newurl/",views.new_url, name="new_url_name"),
    path("newHello", views.htmlHello, name = "html Hello")
]

