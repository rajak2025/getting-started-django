import datetime

from django.shortcuts import render

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "diwali/index.html", {
        "diwali": now.month == 11 and now.date == 4
    })