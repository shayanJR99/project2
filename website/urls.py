from website.views import *
from django.urls import path

urlpatterns = [
    path("",home_view),
    path('about-us', about_view),
    path('contact', contact_view)

]
