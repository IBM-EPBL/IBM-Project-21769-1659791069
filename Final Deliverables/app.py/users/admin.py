from django.contrib import admin
from . models import Members, Office, AboutForm 
from . models import quote
# Register your models here.

admin.site.register(Members)
admin.site.register(Office)
admin.site.register(AboutForm)
admin.site.register(quote)
