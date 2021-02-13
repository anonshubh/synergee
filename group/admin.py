from django.contrib import admin

from .models import Member,Interest,Contact

class CustomAdmin(admin.AdminSite):
    site_header = "Synergee"
    index_title = "Synergee administration"


admin_site = CustomAdmin(name='custom-admin')

admin_site.register(Member)
admin_site.register(Interest)
admin_site.register(Contact)
