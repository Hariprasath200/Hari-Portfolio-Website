from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

def static_urlpatterns():
    return static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    

urlpatterns=[
    path('',views.prasath,name="home"),
    path('about',views.about,name="about"),
    path('certificate',views.certificate,name="certificate"),
    path('project',views.project,name="project"),
    path('contact',views.contact,name="contact"),
] , static_urlpatterns()
       