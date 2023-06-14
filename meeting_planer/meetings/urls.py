from . import views
from django.urls import path
from meetings.views import detail, rooms

urlpatterns = [
    path(''),
    path('<int:id>', detail, name='detail'),
    path('rooms', rooms),
    path('new', views.new, name="new"),
]
