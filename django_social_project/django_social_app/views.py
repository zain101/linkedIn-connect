from django.shortcuts import render

from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa
from django.contrib.auth.models import User

import os
import requests

def login(request):
    context = RequestContext(request)
    # print context
    print "#######################################"
    user  = User.objects.last()
    token = user.social_auth.get(provider='linkedin-oauth2').access_token
    url = 'https://api.linkedin.com/v1/people/~/skills?format=json'
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(url, headers=headers)
    print r.text
    #user.email = r.content.decode("utf-8").strip('"')
    #user.save()

    s = "python /home/zain101/Documents/Django_Stuff/polls/django_social_project/django_social_app/test3.py "+"AQXu4BAozNBlSdjac67qvHsXFlWRVJWePQkabspO3XbarsUVM4p4AepLwjS2bKHIuuchhDfZH3H5TuwHwlOXN8pg3xqSdeeIRrliCaiYKqUOGcsyBup4moU5QvmAAu9dkE202VZH4oDCHh5F5nq13wH-YdEcTI44fmeIdwnUWlZbNV-vnLo"
    os.system(s)
    return render_to_response('login.html', context=context)


def index(request):
    return render_to_response('login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')
