# Third Party Library
from candidate.models import (
    Candidate,
    Education,
    Job,
    Language,
    OtherProject,
    Project,
    Recomendation,
    Skill,
)
from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Job._meta.get_fields()]


class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.get_fields()]


class SkillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Skill._meta.get_fields()]


class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.get_fields()]


class CandidateAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "surname",
        "is_chosen_user",
    ]


class RecomendationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recomendation._meta.get_fields()]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.get_fields()]
    empty_value_display = "-пусто-"


class OtherProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OtherProject._meta.get_fields()]
    empty_value_display = "-пусто-"


admin.site.register(Project, ProjectAdmin)
admin.site.register(OtherProject, OtherProjectAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Recomendation, RecomendationAdmin)

admin.site.unregister(Group)
