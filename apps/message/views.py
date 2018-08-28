# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    #查
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name='bobby',address='北京')
    for message in all_messages:
        print message.name
    #删
    # all_messages = UserMessage.objects.filter(name='bobby',address='北京')
    # all_message.delete()
    # for message in all_messages:
    #     print message.name

    #增
    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('name','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get('email','')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'hl3'
    #     user_message.save()
    return render(request, 'message_form.html')