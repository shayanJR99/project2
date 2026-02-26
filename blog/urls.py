from blog.views import *
from django.urls import path

app_name = "blog"


urlpatterns = [
        path("",home_view,name="home"),
        path('single', blog_single,name="single"),

]
