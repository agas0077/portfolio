# Third Party Library
from candidate.models import (
    Candidate,
    Education,
    HardSkill,
    Job,
    Language,
    OtherProject,
    Project,
    Recomendation,
    SoftSkill,
)
from django.contrib import admin
from django.contrib.auth.models import Group
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Job)
class JobAdmin(TranslationAdmin):
    list_display = [field.name for field in Job._meta.get_fields()]


@admin.register(Language)
class LanguageAdmin(TranslationAdmin):
    list_display = [field.name for field in Language._meta.get_fields()]


@admin.register(HardSkill)
class HardSkillAdmin(TranslationAdmin):
    list_display = [field.name for field in HardSkill._meta.get_fields()]


@admin.register(SoftSkill)
class SoftSkillAdmin(TranslationAdmin):
    list_display = [field.name for field in SoftSkill._meta.get_fields()]


@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = [field.name for field in Education._meta.get_fields()]


@admin.register(Candidate)
class CandidateAdmin(TranslationAdmin):
    list_display = [
        "id",
        "name",
        "surname",
        "is_chosen_candidate",
    ]


@admin.register(Recomendation)
class RecomendationAdmin(TranslationAdmin):
    list_display = [field.name for field in Recomendation._meta.get_fields()]


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = [field.name for field in Project._meta.get_fields()]
    empty_value_display = "-пусто-"


@admin.register(OtherProject)
class OtherProjectAdmin(TranslationAdmin):
    list_display = [field.name for field in OtherProject._meta.get_fields()]
    empty_value_display = "-пусто-"


admin.site.unregister(Group)
