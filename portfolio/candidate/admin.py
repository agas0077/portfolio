from django.contrib import admin
from django.contrib.auth import get_user_model

from candidate.models import (Candidate, Job,
                              Language, Skill,
                              Education, Recomendation)
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
    # def __init__(self, model, admin_site):
    #     print([field.name for field in Recomendation._meta.get_fields()])
    #     super().__init__(model, admin_site)
    list_display = ['id', 'name', 'surname', ]


class RecomendationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recomendation._meta.get_fields()]


admin.site.register(Job, JobAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Recomendation, RecomendationAdmin)
