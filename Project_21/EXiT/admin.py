from EXiT.models import *
from django.contrib import admin

from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.unregister(Site)

admin.site.register(Projet)
admin.site.register(Document)
admin.site.register(Exigence)
admin.site.register(Utilisateur)