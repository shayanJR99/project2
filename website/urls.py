from website.views import *
from django.urls import path

app_name = "website"


urlpatterns = [
    path("",home_view,name="home"),
    path('about', about_view,name="about"),
    path('contact', contact_view,name="contact")

]
