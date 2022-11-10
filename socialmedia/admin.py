from django.contrib import admin

from socialmedia.models import SocialMedias

# Register your models here.


class SocialMediasAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("name", "image", "link")


admin.site.register(SocialMedias, SocialMediasAdmin)
