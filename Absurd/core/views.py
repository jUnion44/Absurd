from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
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
        if c.random:
            responsedict["choices"].append([c.text,random.choice(prompts)["id"]])
        else:
            responsedict["choices"].append([c.text,c.promptNext.id])
        
        
    response = JsonResponse(responsedict)
    return response
