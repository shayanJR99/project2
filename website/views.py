from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about_view(request):
    return HttpResponse("""
                 <h1>hello welcome to our website</h1>
                 <br>
                 <h2>about us : </h2>
                 """)


def home_view(request):
    return HttpResponse("""
                 <h1>hello welcome to our website</h1>
                 <br>
                 <h2>hello home !!!</h2>
                 """)

def contact_view(request):
    return HttpResponse("""
                 <h1>hello welcome to our website</h1>
                 <br>
                 <h2>contact with us</h2>
                 """)
