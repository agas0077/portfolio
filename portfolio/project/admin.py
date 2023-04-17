# Register your models here.
from django.contrib import admin
from project.models import Project, OtherProject
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.get_fields()]
    empty_value_display = '-пусто-'


class OtherProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OtherProject._meta.get_fields()]
    empty_value_display = '-пусто-'


admin.site.register(Project, ProjectAdmin)
admin.site.register(OtherProject, OtherProjectAdmin)