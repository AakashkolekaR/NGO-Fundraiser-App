from django.shortcuts import render
from django.urls import reverse #we used reverse function to use name instead of a url in urls.py
from django.core.files.storage import FileSystemStorage
from employee.models import Event,Employee,Student,Comment
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Sum,Count
from donor.models import Donor,Donations

# Create your views here.

def edashboard(request):
    username=request.session['username']
    d=Employee.objects.get(eusername=username)
    sl=Student.objects.all().aggregate(Count('sname'))['sname__count']
    dl=Donor.objects.all().aggregate(Count('id'))['id__count']
    el=Event.objects.all().aggregate(Count('id'))['id__count']
    f=Donations.objects.all()
    funds=0

    for i in f:
        a=float(i.collectedfunds)
        funds+=a

    




    return render(request,'employee/index.html',{
    'd':d,'sl':sl,'dl':dl,'el':el,'f':funds,
    })

def charte(request):
    uname=request.session['username']
    ee=Employee.objects.get(eusername=uname)
    return render(request,'employee/charte.html',{
    'ee':ee,
    })


def table(request):

    return render(request,'employee/viewstudents.html')

def addevent(request):
    uname=request.session['username']
    ee=Employee.objects.get(eusername=uname)
    return render(request,'employee/addevent.html',{
    'ee':ee,
    })

def addstudent(request):
    uname=request.session['username']
    ee=Employee.objects.get(eusername=uname)
    return render(request,'employee/addstudent.html',{
    'ee':ee,
    })

def events(request):
    event=Event.objects.all()

    p=[]
    n=[]


    for i in event:
        pos=Comment.objects.filter(event_id_id=i.id,sentiment='positive').aggregate(Count('sentiment'))['sentiment__count']
        neg=Comment.objects.filter(event_id_id=i.id,sentiment='negative').aggregate(Count('sentiment'))['sentiment__count']
        p.append(pos)
        n.append(neg)



    sent=zip(p,n,event)
    return render(request,'employee/viewevents.html',{
    'event':sent,'e':event,
    })

def addeventactions(request):
            name=request.POST.get('name','NULL')
            location=request.POST.get('location','NULL')
            address=request.POST.get('address','NULL')
            description=request.POST.get('description','NULL')
            duration=request.POST.get('duration','NULL')
            category=request.POST.get('radios','NULL')
            ev_exfunds=request.POST.get('ev_exfunds','NULL')
            uploadedfileurl=''
            if request.method=='POST' and request.FILES['myfile']:
                myfile=request.FILES['myfile']
                fs=FileSystemStorage()
                filename=fs.save(myfile.name,myfile)
                uploadedfileurl=fs.url(filename)
            s=Event(evname=name,evlocation=location,evaddr=address,evdesc=description,evdur=duration,evpic_path=uploadedfileurl,evtype=category,ev_exfunds=ev_exfunds)
            s.save()
            if s.id:
                return HttpResponseRedirect(reverse('edashboard'))
            else:
                return HttpResponse('Error')

def studentreg(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    contact=request.POST.get('contact')
    address=request.POST.get('address')
    achv=request.POST.get('achv')
    vilcit=request.POST.get('vilcit')
    gender=request.POST.get('radios')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['file']:
        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)


    if contact=='NULL':
        contact=0

    s=Student(sname=name,semail=email,scontact=contact,sadd=address,sprog=achv,scity=vilcit,sgender=gender,spic_path=uploadedfileurl)

    s.save()


    return HttpResponseRedirect(reverse('edashboard'))

def tables(request):
    e=Student.objects.all()
    sr=[]
    for i in range(0,len(e)):
        sr.append(i+1)

    z=zip(e,sr)
    uname=request.session['username']
    ee=Employee.objects.get(eusername=uname)
    return render(request,'employee/viewstudents.html',{
    'e':z,'ee':ee,
    })
