from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import *
import random

STARTER_ID=3

#0=random 1=precoded
CHOICE_SETTING=0

# Create your views here.
def index(request):
    return render(request,"core/index.html",{"starterid":STARTER_ID})

def loadPrompt(request,promptid):
    p = get_object_or_404(Prompt,pk=promptid)
    responsedict = {"prompt":p.text,"choices":[]}
    prompts = list(Prompt.objects.order_by('id').values())
    for c in p.befores.all():
        responsedict["choices"].append([c.text,random.choice(prompts)["id"],c.id])
    responsedict["choices"].append(["Nothing to be done",3,0])
    ch = responsedict["choices"][:]
    random.shuffle(ch)
    responsedict["choices"]=ch
        
    response = JsonResponse(responsedict)
    return response

def loadResponse(request,cid):
    if cid==0:
        return JsonResponse({"l":[""]})
    else:
        c = get_object_or_404(Choice,pk=cid)
        lines = c.response.splitlines()
        return JsonResponse({"l":lines})
def void(request):
    return render(request,"core/void.html",{"starterid":STARTER_ID})
