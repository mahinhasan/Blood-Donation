from os import name
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponseRedirect
from .form import*
from br.models import BloodRequest
from django.urls import reverse
from django.db.models import Q
from .models import*
# from twilio.rest import Client
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import EmptyPage, Paginator,PageNotAnInteger,Page
from .hospital import hospitals
from .ambulance import ambulances
from .doners import*
# import folium
# import geocoder


#signpu django




# Create your views here.
def home(request):

    # location = geocoder.osm('BD/JAMALPUR')

    # lat = location.lat
    # lng = location.lng
    # country = location.country
    # f = folium.Map(location=[23.6850,90.3563],zoom_start=6)
    # folium.Marker([24.9250,89.9463],tooltip = "Bangladesh").add_to(f)
    # folium.Marker([lat,lng],tooltip = country).add_to(f)

    # f = f._repr_html_()



    doner = BloodDoner.objects.all()
    post = CreatePost.objects.all().order_by('-time')
    total = BloodDoner.objects.all().count()
    recent_request = BloodRequest.objects.all().order_by('-time')[:3]
    
    all_post = Paginator(post,3)
    page = request.GET.get('page')

    try:
        post = all_post.page(page)
    except PageNotAnInteger:
        post = all_post.page(1)
    except EmptyPage:
        post = all_post.page(all_post.num_pages)

    # for d in doner:
    #     g = d.group
    # gr  = request.POST.get('g')        
    # print(gr)
    # if g == gr:
    #     print("Yes its match!")
    # else:
    #     print("please insert correct input!")
    return render(request,'blood/index.html',{'post':post,'total':total,'recent_requests':recent_request})


def blood_request_post_detail(request,id):
    post = CreatePost.objects.all().order_by('-time')

    allPost = get_object_or_404(CreatePost,pk=id)

    latest_post = Paginator(post,7)
    page = request.GET.get('page')

    try:
        post = latest_post.page(page)
    except PageNotAnInteger:
        post = latest_post.page(1)
    except EmptyPage:
        post = latest_post.page(latest_post.num_pages)
    return render(request,'blood/post_request_detail.html',{'latest': post,'posts':allPost})

def add_blood_doner(request):
    fm = DonerForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
       
        fm = DonerForm(request.POST,request.FILES)
        if fm.is_valid():
            accout_sid = "AC4b78ecc8f287ae52055e3e572cb6f710"
            auth_token = "5a38a9b56e30e66ebf8c9a567debbc38"
            # client = Client(accout_sid,auth_token)
            # client.messages.create(from_="+12029536456",body="Sir there need your blood!",to="+880-1315091449")
            send_mail('Welcome to blood.com '+str(name), 'Thanks for register as a Doner !', 'mahinhasanaiub@gmail.com', [email],
                fail_silently=False)
            fm.save()
        return HttpResponseRedirect ('/')
    return render(request,'blood/doner_add.html',{'form':fm})


def blood_request_post(request):
    gr = request.POST.get('group')
    dis = request.POST.get('district')
    doner = BloodDoner.objects.filter(group=gr)
    # print(doner)
    x = []
    addr=[]
    for d in doner:
        # print(d.group)
        # print(d.email)
        e = d.email
        addr.append(d.district)
        x.append(e)
    #print(addr)
    # print("Email: ",x)
    create = CreateForm()
    if request.method=='POST':
        create = CreateForm(request.POST,request.FILES)
        if create.is_valid():
            for adr in addr:
                if dis==adr:
                    accout_sid = "AC4b78ecc8f287ae52055e3e572cb6f710"
                    auth_token = "5a38a9b56e30e66ebf8c9a567debbc38"
                    # client = Client(accout_sid,auth_token)
                    client.messages.create(from_="+12029536456",body="Sir there need your blood!",to="+880-1749809704")
                    
                    send_mail('Hello dost we need your '+gr+ ' blood ', 'Emergancy', 'mahinhasanaiub@gmail.com', x,
                fail_silently=False)
            create.save()
            return HttpResponseRedirect ('/')
    context = {'form':create}
        
    return render(request,'blood/create_post.html',context)



def all_blood_request_list(request):
    all = CreatePost.objects.all().order_by('-time')
    return render(request,'blood/all_post.html',{'posts':all})

def all_blood_request_detail(request,id):
    post = get_object_or_404(BloodRequest,pk=id)
    author = request.user
    email = request.POST.get('email')
    msg = request.POST.get('message')
    remail = BloodRequest.objects.filter(id=id) #recevier email
    receiver = []
    for r in remail:
        receiver.append(r.email)

    # print(remail)
    # # print(author,email,msg)
    if request.method=='POST':

        send_mail('Response from blood doner upon your request',msg,email ,receiver,
                fail_silently=False)
    # return render(request,'blood/request_detail.html',{'post':post})
    return render(request,'blood/post_request_detail.html',{'post':post})

def delete_request_post(request,id):
    post = BloodRequest.objects.get(pk=id)
    if request.method=='POST':
        post = BloodRequest.objects.get(pk=id)
        post.delete()

        return redirect('b_request')
    return render(request,'blood/delete_post.html',{'post':post} )

def update_request_post(request,id):
    post = BloodRequest.objects.get(id=id)
    form = CreateForm(instance=post)
    if request.method=='POST':
        form = CreateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('b_request')
        else:
            
            form = CreateForm()

    return render(request,'blood/update_post.html',{'post':post,'form':form})


def doner(request):
    form = blood_doners(request.POST)
    doners = BloodDoner.objects.all()
    if request.method=='POST':

        form = blood_doners(request.POST,queryset=doners)
        doners = form.qs
    else:
        doners = BloodDoner.objects.all()
    return render(request,'blood/doner_list.html',{'form':form,'doners':doners})

# def search_doner(request):
#     doners = BloodDoner.objects.all() 
#     form = SearchForm(request.GET)
#     group = request.GET.get('group')
#     district = request.GET.get('district')
#     if group !='' and group is not None:
#         doners = doners.filter(group=group)
#     elif district !='' and district is not None:
#         doners = doners.filter(district=district)    

#     elif (group !='' and group is not None) and (district !='' and district is not None) :
#         doners = doners.filter(group=group , district=district)
    
#     else:
#         doners = BloodDoner.objects.all()
#     form = SearchForm()
#     return render(request,'blood/doner_list.html',{'doners':doners,'form':form})


def hospital(request):
    form = hospitals(request.POST)
    hptls = Hospital.objects.all()
    if request.method=='POST':
        form = hospitals(request.POST,queryset=hptls)
        hptls = form.qs
    else:
        hptls = Hospital.objects.all()
    return render(request,'blood/hospital.html',{'form':form,'hptls':hptls})

def add_hospital_ambulance(request):
    fm = HospitalAddForm()
    if request.method == 'POST':
        fm = HospitalAddForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect ('/')
    return render(request,'blood/add_hospital.html',{'form':fm})


# def hospital_and_ambulance_search(request):

#     hospital = Hospital.objects.all()
#     form = HospitalForm(request.GET)

#     name = request.GET.get('name')
#     district = request.GET.get('district')

#     if (name !='' and name is not None) and (district !='' and district is not None) :
#         hospital = hospital.filter(name__icontains=name , district=district)
#     form = HospitalForm()
#     return render(request,'blood/hospital.html',{'hospitals':hospital,'form':form})

def add_ambulance(request):
    fm = AmbulanceAddForm()
    if request.method == 'POST':
        fm = AmbulanceAddForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect ('/')
    return render(request,'blood/add_ambulance.html',{'form':fm})


def ambulance_search(request):

    form = ambulances(request.POST)
    ambulance= Ambulance.objects.all()
    if request.method=='POST':
        form = ambulances(request.POST,queryset=ambulance)
        ambulance = form.qs
    else:
        ambulance = Ambulance.objects.all()
    return render(request,'blood/ambulance.html',{'form':form,'ambulance':ambulance})