from django.shortcuts import render
import datetime
from .models import *
# Create your views here.
def prasath(request):
    message = 'GOOD'
    date = datetime.datetime.now()
    hour  = int(date.strftime('%H')) 
    if hour<12:
        message+=' MORNING'
    elif hour<16:
         message+=' AFTERNOON'
    else:
        message+= ' EVENING'
    
    name = "hari"
    date_dict = {'dict':date,'nam_e':name,'greetings':message}
    return render(request, 'hari.html', context= date_dict)


def about(request):
    message = 'GOOD'
    date = datetime.datetime.now()
    hour  = int(date.strftime('%H')) 
    if hour<12:
        message+=' MORNING'
    elif hour<16:
         message+=' AFTERNOON'
    else:
        message+= ' EVENING'
    
    name = "hari"
    date_dict = {'dict':date,'nam_e':name,'greetings':message}
    
    return render(request,"aboutpage.html", context= date_dict)
def contact(request):
    message = 'GOOD'
    date = datetime.datetime.now()
    hour  = int(date.strftime('%H')) 
    if hour<12:
        message+=' MORNING'
    elif hour<16:
         message+=' AFTERNOON'
    else:
        message+= ' EVENING'
    
    name = "hari"
    date_dict = {'dict':date,'nam_e':name,'greetings':message}
    return render(request,"contact.html",context= date_dict)
def certificate(request):   
    message = 'GOOD'
    date = datetime.datetime.now()
    hour  = int(date.strftime('%H')) 
    if hour<12:
        message+=' MORNING'
    elif hour<16:
         message+=' AFTERNOON'
    else:
        message+= ' EVENING'
    
    name = "hari"
    date_dict = {'dict':date,'nam_e':name,'greetings':message}
    return render(request,"certificate.html",context=date_dict)
def project(request):
    message = 'GOOD'
    date = datetime.datetime.now()
    hour  = int(date.strftime('%H')) 
    if hour<12:
        message+=' MORNING'
    elif hour<16:
         message+=' AFTERNOON'
    else:
        message+= ' EVENING'
    
    name = "hari"
    date_dict = {'dict':date,'nam_e':name,'greetings':message}
    return render(request,"project.html",context=date_dict)




