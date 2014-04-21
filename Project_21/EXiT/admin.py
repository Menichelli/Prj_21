from EXiT.models import *
from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Projet)
admin.site.register(Document)
admin.site.register(Exigence)