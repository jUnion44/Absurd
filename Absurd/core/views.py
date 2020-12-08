from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

STARTER_ID=3

# Create your views here.
def index(request):
    return render(request,"core/index.html",{"starterid":STARTER_ID})

def loadPrompt(request,promptid):
    p = get_object_or_404(Prompt,pk=promptid)
    responsedict = {"prompt":p.text,"choices":[]}
    for c in p.befores.all():
        responsedict["choices"].append([c.text,c.promptNext.id])
    response = JsonResponse(responsedict)
    return response
