from django.contrib import admin

from services.models import Services

# Register your models here.


class ServicesAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("title", "description")


admin.site.register(Services, ServicesAdmin)
