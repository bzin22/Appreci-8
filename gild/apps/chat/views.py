import bleach
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.core.mail import send_mail

from gild import settings
from .forms import ChatForm

def ShowChatHome(request):
    return render(request,"chat_home.html")

def ShowChatPage(request, room_name, person_name):
    return render(request, "chat_screen.html",{'room_name':room_name,'person_name':person_name})
    # return HttpResponse("Chat page"+" "+room_name+" "+person_name)