from django.contrib import admin

from getintouch.models import Messages

# Register your models here.

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    # model = CustomUser
    list_display = ("full_name", "email_address", "subject", "is_visited")


admin.site.register(Messages, MessagesAdmin)
