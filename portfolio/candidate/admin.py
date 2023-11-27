# Standard Library
from collections.abc import Sequence

# Third Party Library
from candidate.models import (
    Candidate,
    Education,
    File,
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
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

# Register your models here.


class BaseTranslationAdmin(TranslationAdmin):
    empty_value_display = _("-empty-")

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        self.model
        return [
            field.name
            for field in self.model._meta.get_fields()
            if not field.many_to_many
        ]


@admin.register(Candidate)
class CandidateAdmin(TranslationAdmin):
    list_display = [
        "title",
        "is_chosen_candidate",
    ]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in File._meta.get_fields()]


@admin.register(Job)
class JobAdmin(TranslationAdmin):
    list_display = [
        "title",
        "company",
    ]


@admin.register(OtherProject)
class OtherProjectAdmin(TranslationAdmin):
    list_display = [
        "title",
    ]


@admin.register(Project)
class ProjectAdmin(BaseTranslationAdmin):
    list_display = [
        "title",
    ]


@admin.register(Language)
class LanguageAdmin(BaseTranslationAdmin):
    pass


@admin.register(HardSkill)
class HardSkillAdmin(BaseTranslationAdmin):
    pass


@admin.register(SoftSkill)
class SoftSkillAdmin(BaseTranslationAdmin):
    pass


@admin.register(Education)
class EducationAdmin(BaseTranslationAdmin):
    pass


@admin.register(Recomendation)
class RecomendationAdmin(BaseTranslationAdmin):
    pass


admin.site.unregister(Group)
