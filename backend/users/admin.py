from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name',)
    list_filter = ('email', 'first_name')


admin.site.register(User, UserAdmin)