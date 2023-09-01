from django.contrib import admin

from .models import Link, Profile


# customize the display admin
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Link)
