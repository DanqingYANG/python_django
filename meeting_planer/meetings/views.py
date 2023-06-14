from django.shortcuts import render, get_object_or_404
from .models import Meeting
from django.forms import modelform_factory

# Create your views here.
def detail(require,id):
    meeting = Meeting.objects.get(pk=id)
    return render(require, "meetings/detail.html", {'meeting':meeting})

# Add a page that shows a list of all room objects
def rooms(require):
    meetings = Meeting.objects.all()
    return render(require, "meetings/rooms.html", {'meetings': meetings})

# Add user interface with Modelform
# Generate html forms by using Meeting as the input object
MeetingForm = modelform_factory(Meeting, exclude=[]) # MeetingForm is a class not object

def new(request):
    form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})