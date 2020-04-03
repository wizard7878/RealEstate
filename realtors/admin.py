from django.contrib import admin
from realtors.models import Realtor
# Register your models here.

@admin.register(Realtor)
class AdminRealtor(admin.ModelAdmin):
    list_display = ('id','name','email','phone','is_mvp','hire_date')
    list_editable = ('is_mvp',)
    list_filter = ('name','is_mvp','hire_date')
    list_per_page = 6
    list_display_links = ('name',)
