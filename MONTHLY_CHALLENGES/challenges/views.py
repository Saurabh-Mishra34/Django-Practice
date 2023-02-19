from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


#dictionary to make views responsive
month_dict = {
    
    "january": "january is the month",
    "february": "february is the month",
    "march": "march is the month",
    "april": "april is the month",
    "may": "may is the month",
    "june": "june is the month",
    "july": "july is the month",
    "august": "august is the month",
    "september": "september is the month",
    "october": "ocotber is the month",
    "november": "november is the month",
    "december": "december is the month",
    
}



# Create your views here.
def pracWebmon(request,imon):
    inp_month = imon
    
    if  inp_month <= 12 :
        return HttpResponse(f'{imon}')
    
    else:
        return HttpResponseNotFound('<h1>Page no where</h1>')

def pracWeb(request,month):
    
    try:
        return HttpResponse(f'{month_dict[month]}')
    except:
        return HttpResponseNotFound('<h1>Page not found</h1>')