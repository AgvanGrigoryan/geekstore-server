from django.contrib import admin

from users.models import User
from products.admin import BasketAdminInline

# admin.site.register(User)


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    inlines = (BasketAdminInline,)

