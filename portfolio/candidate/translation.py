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
from modeltranslation.translator import register, TranslationOptions


@register(Candidate)
class CandidateTranslationOption(TranslationOptions):
    fields = [
        "name",
        "surname",
        "search_job_title",
        "city",
        "country",
        "about",
        "about_skills",
    ]


@register(Job)
class JobTranslationOption(TranslationOptions):
    fields = ["title", "description", "company"]


@register(Skill)
class SkillTranslationOption(TranslationOptions):
    fields = [
        "title",
        "tooltip",
    ]


@register(Education)
class EducationTranslationOption(TranslationOptions):
    fields = [
        "title",
        "place",
    ]


@register(Language)
class LanguageTranslationOption(TranslationOptions):
    fields = [
        "title",
        "level",
    ]


@register(Recomendation)
class RecomendationTranslationOption(TranslationOptions):
    fields = [
        "text",
        "author",
        "author_job_title",
    ]


@register(OtherProject)
class OtherProjectTranslationOption(TranslationOptions):
    fields = [
        "title",
        "description",
    ]


@register(Project)
class ProjectTranslationOption(TranslationOptions):
    fields = [
        "title",
        "description",
    ]
