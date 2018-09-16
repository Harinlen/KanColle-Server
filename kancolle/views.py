import execjs
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from . import battle

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index. ")

def startBattle(request):
    result = battle.startBattle()
    return JsonResponse(result)