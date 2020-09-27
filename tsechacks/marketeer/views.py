from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from employee.models import marketeer,Event
from donor.models import Donor
# Create your views here.

def mdashboard(request):
    mname = request.session['username']
    m = marketeer.objects.get(musername = mname)
    return render(request,'marketeer/index.html',{'market':m})



def table(request):
    mname = request.session['username']
    m = marketeer.objects.get(musername = mname)

    e = Event.objects.all()
    return render(request,'marketeer/table.html',{'event':e,'market':m})

def table1(request):
    mname = request.session['username']
    m = marketeer.objects.get(musername = mname)
    d = Donor.objects.all()
    return render(request,'marketeer/table1.html',{'donor':d,'market':m})




def sendmail(request):
    mname = request.session['username']
    m = marketeer.objects.get(musername = mname)

    return render(request,'marketeer/sendmail.html',{'market':m})

def sendmaile(request):
    try:
        subject = 'Event notification'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tendulkaramey@gmail.com']
        print('working')
        send_mail( subject, message, email_from, recipient_list , fail_silently=True)
    except:
        print('error')
    finally:
        return HttpResponseRedirect(reverse('sendmail'))
