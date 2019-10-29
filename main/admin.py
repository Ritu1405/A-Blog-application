from django.contrib import admin
from .models import Website, Comment

# Register your models here.
class WebsiteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("List_display" , {"fields" : ["title", "slug", "created_date"]}),
        ("Content", {"fields" : ["text"]})
    ]       

admin.site.register(Website , WebsiteAdmin)           
admin.site.register(Comment)



