# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name='bobby')
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html',{
        "my_message":message
    })