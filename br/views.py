from django.shortcuts import get_object_or_404, render
from .models import BloodRequest
from twilio.rest import Client

from blood.models import BloodDoner
from .form import BloodRequestForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required(login_url='login')
def home(request): 
    posts = BloodRequest.objects.all()
      

    group = request.POST.get('blood_group')
    mail = request.POST.get('email')
    contact = request.POST.get('contact')
    district = request.POST.get('district')
    doners = BloodDoner.objects.filter(group=group)
    
    mails = []
    districts = []
    contacts = []

    for mail in doners:
        mails.append(mail.email)
        districts.append(mail.district)
        contacts.append(mail.phone)

    
    # print(mails,districts,contacts)
    
    if request.method =='POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            for d in districts:
                if d == district:
                    accout_sid = "AC4b78ecc8f287ae52055e3e572cb6f710"
                    auth_token = "5a38a9b56e30e66ebf8c9a567debbc38"
                    client = Client(accout_sid,auth_token)
                    # client.messages.create(from_="+12029536456",body="Sir there need your blood!",to=[contacts])
                    
                    send_mail('Hello doner we need your '+group+ ' blood ', 'Emergancy', 'mahinhasanaiub@gmail.com', mails,
                fail_silently=False)
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form = BloodRequestForm()
    else:
        form = BloodRequestForm()

    context = {
        'posts':posts,
        'form':form,
    }

    return render(request,'br/create_post.html',context)

    
# def all_blood_request_detail(request,id):
#     posts = get_object_or_404(BloodRequest,pk=id)

#     return render(request,'blood/request_detail.html',{'posts':posts})