
from django.shortcuts import render
from .models import Contact,Service,Aboutm,Postcmnt
from django.http import HttpResponse

def home(request):
    whole_service = Service.objects.all()
    whole_msg = Postcmnt.objects.all()
    params = {'service': whole_service,'messege': whole_msg}

    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        secondname = request.POST.get('secondname', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        tarea = request.POST.get('tarea', '')
        txarea = request.POST.get('txtarea', '')
        user = request.user
        print(firstname, secondname, phone, email, tarea)
        contact = Contact(firstname=firstname, secondname=secondname, phone=phone, email=email, msg=tarea )
        cmntbox = Postcmnt( msg=txarea,user=user)
        contact.save()
        cmntbox.save()


    return render(request,'ptf/home.html',params)



def about(request):
    abt=Aboutm.objects.all()
    para={'abot':abt}
    return render(request,'ptf/about.html',para)

def blog(request):
    return render(request , 'ptf/blog.html')
