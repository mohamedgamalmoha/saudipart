from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Robbery


admin.site.register(Robbery)
admin.site.unregister(User)
admin.site.unregister(Group)
