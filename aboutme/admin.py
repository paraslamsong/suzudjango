from django.contrib import admin

from aboutme.models import AboutMe, Greetings

# Register your models here.


class AboutMeAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("about", "resume")


admin.site.register(AboutMe, AboutMeAdmin)


class GreetAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("greet", "resignation", "description")


admin.site.register(Greetings, GreetAdmin)
