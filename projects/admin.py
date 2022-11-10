from django.contrib import admin

from projects.models import Projects

# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("name", "image")


admin.site.register(Projects, ProjectsAdmin)
