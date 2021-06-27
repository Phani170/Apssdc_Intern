from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
    return HttpResponse('Hi Good Evening to All..')

def h2tag(re):
    return HttpResponse('<h2>Welcome to the header</h2>')

def welcomeUser(usr,uname):
    return HttpResponse("<h2>Hi ,Welcome <span style='color:green'>{}</span></h2>".format(uname))

def welcomeUser2(usr,uname,uno):
    return HttpResponse('''
    <script>alert('Hi, Welcome {0}')</script>
    <h2 align='center'>Hi ,Welcome <span style='color:green'>{0}</span> your no is <span style='color:blue'>{1}</span>
    </h2>
    '''.format(uname,uno))

def htm(request):
    return render(request,'html/sample.html')

def name(req,uname):
    return render(req,'html/name.html',{'n':uname})

def ename(request,id,ename):
    k={'i':id,'n':ename}
    return render(request,'html/ename.html',k)

def form(request):
    return render(request,'html/sampleForm.html')

def alert(request):
    return render(request,"html/alert.html")

def myform(req):
    if req.method=="POST":
        uname= req.POST['uname']
        rollno= req.POST['rollno']
        email=req.POST.get('email')
        print(uname,rollno,email)
        data={'username':uname,'rollno':rollno,'email':email}
        return render(req,'html/myformaction.html',data)

    return render(req,'html/myform.html')

def bootstrap(req):
    return render(req,'html/sampleboot.html')

def bstreg(req):
    return render(req,'html/bstreg.html')

def register1(req):
    reg = Register(name="siva",email="siva@gmail.com")
    reg.save()
    return HttpResponse("row inserted successfully")

def register2(req):
    if req.method=="POST":
        name= req.POST['name']
        email= req.POST.get('email')
        reg=Register(name=name,email=email)
        reg.save()
        return HttpResponse("Record inserted successfully")

    return render(req,'html/register2.html')

def display1(req):
    data = Register.objects.all()

    return render(req,'html/display1.html',{'data':data})

def sview(req,y):
    w=Register.objects.get(id=y)
    return render(req,'html/sview.html',{'y':w})

def sup(req,y):
    w=Register.objects.get(id=y)
    if req.method=="POST":
        na= req.POST['n']
        em= req.POST['e']
        w.name=na
        w.email=em
        w.save()
        return redirect('/display1')

    return render(req,'html/sup.hmtl',{'y':w})