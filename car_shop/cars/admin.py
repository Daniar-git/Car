from django.contrib import admin
from .models import Cars

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    # fields = ['year','brand']
    fieldsets = [
        ('Time information',{'fields':['year']}),
        ('Car information',{'fields':['brand']}),
    ]

admin.site.register(Cars,CarAdmin)