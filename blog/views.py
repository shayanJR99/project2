from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, "blog/blog-home.html")

def blog_single(request):
    return render(request, "blog/blog-single.html")
