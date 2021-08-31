from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Thief, Victim


admin.site.register(Thief)
admin.site.register(Victim)
admin.site.unregister(User)
admin.site.unregister(Group)
