from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.
'''

def welcome(request):
    # "website/welcome.html" is not url but templates/website/welcome.html
    #return render(request, "website/welcome.html")
    
    # Get the number of meetings
    #cnt = Meeting.objects.count()
    #return render(request, "website/welcome.html", {"cnt":cnt})    
'''

# Get object or 404
from django.shortcuts import get_object_or_404

def welcome(request):
    cnt = Meeting.objects.count()
    return render(request, "website/welcome.html", {'cnt': cnt})
    # a list of meetings



def about(request):
    return HttpResponse("1. New a project with PyCharm. 2. Install django "
                        "3. Startproject 'meeting_planer' with django "
                        "4. Enter meeting_planer 5. Enter first level, "
                        "add a startapp by using python m"
                        "anage.py startapp folder")