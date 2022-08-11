from urllib import request
from urllib import request
from django.shortcuts import render
from .models import FeedBack
from django.contrib import messages

def home(request):
    return render(request, 'trail.html')

def trail1(request):
    return render(request, 'trail1.html')

def trail2(request):
    return render(request, 'trail2.html')

def trail3(request):
    return render(request, 'trail3.html')

def trail4(request):
    return render(request, 'trail4.html')

def trail6(request):
    return render(request, 'trail6.html')

def trail7(request):
    return render(request, 'trail7.html')

def trail5(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feed = request.POST.get('feed')

        new_feed = FeedBack.objects.create(name=name,email=email,phone=phone,feed=feed)
        new_feed.save()
        messages.success(request, 'Feedback Successfully Submitted')

    return render(request, 'trail5.html')



