from django.contrib import admin

from silicontech.models import Contact


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ProjectAdmin)