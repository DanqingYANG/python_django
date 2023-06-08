from django.contrib import admin
from meetings.models import Meeting, Room

# Register your models here.
# to migrate
admin.site.register(Meeting)
admin.site.register(Room)