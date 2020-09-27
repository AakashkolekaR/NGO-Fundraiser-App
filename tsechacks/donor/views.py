from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse #we used reverse function to use name instead of a url in urls.py
from django.core.files.storage import FileSystemStorage
from donor.models import Donor,Donations
from employee.models import Employee,Event,Comment,Likes,marketeer
#from donor import sentimentanalysis
# Create your views here.
def donordashboard(request):
    username=request.session['username']
    d=Donor.objects.get(username=username)
    return render(request,'donor/index.html',{
    'd':d
    })

def donations(request):
    username=request.session['username']
    d=Donor.objects.get(username=username)
    u=Donations.objects.filter(donor_id=d.id)
    print(u)
    l=[]
    for i in u:
        print(i.donationtype)
        e=Event.objects.get(id=i.event_id_id)
        l.append(e)
    max=zip(u,l)
    return render(request,'donor/table.html',{'max':max,})

def donorevents(request):
    event=Event.objects.all()
    return render(request,'donor/event.html',{
    'event':event
    })

def eventdesc(request,eid):
    s=Event.objects.get(id=eid)
    username=request.session['username']
    e=Event.objects.filter(id=eid)
    comment=Comment.objects.filter(event_id_id=eid)
    like1=Likes.objects.filter(username=username,event_id_id=eid)
    if len(like1):
        liked=1
    else:
        liked=0

    print(comment)
    return render(request,'donor/eventdesc.html',{
    's':s,'username':username,'c':comment,'liked':liked,
    })

def donorregister(request):
    return render(request,'donor/register.html')

def login(request):
    return render(request,'donor/login.html')

def registeraction(request):
        name=request.POST.get('name','NULL')
        email=request.POST.get('email','NULL')
        contactno=request.POST.get('contactno','NULL')
        username=request.POST.get('username','NULL')
        password=request.POST.get('password','NULL')
        uploadedfileurl=''
        if request.method=='POST' and request.FILES['myfile']:
            myfile=request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            uploadedfileurl=fs.url(filename)

        bool=usernamepresent(username)
        if contactno=='NULL':
            contactno=0
        if bool==True:
            s=Donor(dname=name,email=email,contact=contactno,username=username,password=password,pic_path=uploadedfileurl)

            s.save()
            if s.id:
                '''subject = 'Registered'
                message = 'Thank you for Registering -Philantrophers Inc'
                from_email = settings.EMAIL_HOST_USER
                li=[email]

                a=send_mail(subject,message,from_email,li,fail_silently = True)'''

                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponse('Error')

        else:
            return HttpResponseRedirect(reverse('donorregister'))

def usernamepresent(username):
    if Donor.objects.filter(username=username).exists():
        return False
    else:
        return True


def loginaction(request):
    username=request.POST['username']
    password=request.POST['password']

    l= Donor.objects.filter(username=username,password=password)

    if len(l):
        request.session['username']=username #session started
        return HttpResponseRedirect(reverse('donordashboard'))

    e=Employee.objects.filter(eusername=username,epassword=password)
    if len(e):
        request.session['username']=username
        return HttpResponseRedirect(reverse('edashboard'))

    m=marketeer.objects.filter(musername=username,mpassword=password)
    if len(m):
        request.session['username']=username
        return HttpResponseRedirect(reverse('mdashboard'))
    else:

        return HttpResponseRedirect(reverse('login')+'?login_failure=true')

def logoutaction(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))

def money_donation(request,sid):
    print(sid)
    e=Event.objects.get(id=sid)
    money=request.POST.get('money','NULL')
    username=request.session['username']
    d=Donor.objects.get(username=username)
    so=Donations(donor_id=d,event_id=e,collectedfunds=money,donationtype='money')
    so.save()
    if so.id:
        return HttpResponseRedirect(reverse('donordashboard'))
    else:
        return HttpResponse('Error')

def food_donation(request,sid):
    print(sid)
    e=Event.objects.get(id=sid)
    money=int(request.POST.get('food','NULL'))*100
    username=request.session['username']
    d=Donor.objects.get(username=username)
    so=Donations(donor_id=d,event_id=e,collectedfunds=str(money),donationtype='food')
    so.save()
    if so.id:
        return HttpResponseRedirect(reverse('donordashboard'))
    else:
        return HttpResponse('Error')

def stationary_donation(request,sid):
    print(sid)
    e=Event.objects.get(id=sid)
    money=int(request.POST.get('stationary','NULL'))*100
    username=request.session['username']
    d=Donor.objects.get(username=username)
    so=Donations(donor_id=d,event_id=e,collectedfunds=str(money),donationtype='stationary')
    so.save()
    if so.id:
        return HttpResponseRedirect(reverse('donordashboard'))
    else:
        return HttpResponse('Error')


def commententer(request):
    username=request.session['username']
    comment=request.POST.get('comment','NULL')
    pid1=request.POST.get('pid','NULL')
    sp=Event.objects.get(id=pid1)
    ccc=[]
    ccc.append(comment)
    #print(ccc.shape)

    #print(twt)
    ans=1
    #ans=sentimentanalysis.sentiment(ccc)
    #print(ans)
    if ans==0:
        a='negative'
    else:
        a='positive'


    c=Comment(username=username,event_id=sp,comment=comment,sentiment=a)
    c.save()

    return HttpResponseRedirect(reverse('eventdesc',args=[pid1]))

def likeadd(request):
    username=request.session['username']
    pid=request.POST['pid']
    sp=Event.objects.get(id=pid)

    l=Likes(username=username,event_id_id=sp.id)

    l.save()
    print(pid)
    return HttpResponseRedirect(reverse('eventdesc', args=[pid]))


def download_cert(request,eid):
    username=request.session['username']
    doner=Donor.objects.get(username=username)
    e=Event.objects.get(id=eid)
    d=Donations.objects.get(id=eid,donor_id=doner.id)
    return render(request,'donor/download_cert.html',{'username':username,'e':e,'d':d})
