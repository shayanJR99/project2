from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    data = {"author":"shayanJR",
            "title" : "buy bitcoin",
            "paragraph":"buy bitcoin because it reached from 120,000 to 64,000 !!!"
            }
    
    return render(request, 
                  "blog/blog-home.html",
                  data
                  )

def blog_single(request):
    return render(request, "blog/blog-single.html")
