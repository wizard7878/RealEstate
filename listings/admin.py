from django.contrib import admin
from listings import models
# Register your models here.

@admin.register(models.Listing)
class AdminListing(admin.ModelAdmin):
    list_display = ('id','title', 'realtor', 'city', 'price', 'is_publised','list_date',)
    list_editable = ('is_publised',)
    list_filter = ('realtor', 'is_publised',)
    list_per_page = 6
    list_display_links = ('title',)




@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','name','user','active','pub_date')
    list_filter = ('active','pub_date','user')
    list_display_links = ('id','name',)
    list_editable = ('active',)
