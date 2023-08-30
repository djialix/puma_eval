from django.shortcuts import render
from datetime import datetime

def index(request):

    return render(request, "eval/index.html", context={})