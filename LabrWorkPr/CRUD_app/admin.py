from django.contrib import admin
from .models import socialNetworks, socialNetworks_types

# Register your models here.

admin.site.register(socialNetworks)  
admin.site.register(socialNetworks_types)