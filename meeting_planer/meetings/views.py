from django.shortcuts import render, get_object_or_404
from .models import Meeting

# Create your views here.
def detail(require,id):
    meeting = Meeting.objects.get(pk=id)
    return render(require, "meetings/detail.html", {'meeting':meeting})

# Add a page that shows a list of all room objects
def rooms(require):
    meetings = Meeting.objects.all()
    return render(require, "meetings/rooms.html", {'meetings': meetings})