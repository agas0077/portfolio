# Standard Library
from collections.abc import Sequence

from django.template.response import TemplateResponse

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
    Stack,
    Ip,
)
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from candidate.services import (
    count_chosen_candidate_ips,
    count_chosen_candidate_unique_ips,
    count_ips,
    count_unique_ips,
)

User = get_user_model()


class CustomAdminSite(AdminSite):
    def index(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        extra_context["unique_ips_count"] = count_unique_ips()
        extra_context["total_ips_count"] = count_ips()
        return super().index(request, extra_context)


custom_admin_site = CustomAdminSite("custom_admin_site")


class BaseTranslationAdmin(TranslationAdmin):
    empty_value_display = _("-empty-")

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:
        self.model
        return [
            field.name
            for field in self.model._meta.get_fields()
            if not field.many_to_many
        ]


class CandidateAdmin(TranslationAdmin):
    list_display = [
        "title",
        "is_chosen_candidate",
        "views_count",
        "views_count_unique",
    ]

    def views_count_unique(self, obj):
        result = count_chosen_candidate_unique_ips(obj)
        return result

    def views_count(self, obj):
        result = count_chosen_candidate_ips(obj)
        return result

    views_count_unique.short_description = _("Unique views count")
    views_count.short_description = _("Views count")


class FileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in File._meta.get_fields()]


class JobAdmin(TranslationAdmin):
    list_display = [
        "title",
        "company",
    ]


class OtherProjectAdmin(TranslationAdmin):
    list_display = [
        "title",
    ]


class ProjectAdmin(TranslationAdmin):
    list_display = [
        "title",
        "finish_date",
    ]


class LanguageAdmin(BaseTranslationAdmin):
    pass


class HardSkillAdmin(BaseTranslationAdmin):
    pass


class SoftSkillAdmin(BaseTranslationAdmin):
    pass


class EducationAdmin(BaseTranslationAdmin):
    pass


class RecomendationAdmin(BaseTranslationAdmin):
    pass


class StackAdmin(BaseTranslationAdmin):
    pass


class IpAdmin(admin.ModelAdmin):
    list_display = [
        "ip",
        "view_datetime",
        "candidate",
    ]


custom_admin_site.register(Candidate, CandidateAdmin)
custom_admin_site.register(Education, EducationAdmin)
custom_admin_site.register(File, FileAdmin)
custom_admin_site.register(HardSkill, HardSkillAdmin)
custom_admin_site.register(Job, JobAdmin)
custom_admin_site.register(Language, LanguageAdmin)
custom_admin_site.register(OtherProject, OtherProjectAdmin)
custom_admin_site.register(Project, ProjectAdmin)
custom_admin_site.register(Recomendation, RecomendationAdmin)
custom_admin_site.register(SoftSkill, SoftSkillAdmin)
custom_admin_site.register(Stack, StackAdmin)
custom_admin_site.register(Ip, IpAdmin)
custom_admin_site.register(User, UserAdmin)
