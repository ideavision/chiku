from django.contrib import admin
from . models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date')
    search_fields=('name',)
    list_filter=('hire_date',)
admin.site.register(Realtor,RealtorAdmin)

# Register your models here.
