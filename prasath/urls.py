from django.urls import path
from . import views

urlpatterns=[
    path('',views.prasath,name="home"),
    path('about',views.about,name="about"),
    path('certificate',views.certificate,name="certificate"),
    path('project',views.project,name="project"),
    path('contact',views.contact,name="contact"),
]