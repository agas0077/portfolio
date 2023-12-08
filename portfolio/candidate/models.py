# Standard Library
import re

# Third Party Library
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class Candidate(models.Model):
    """Модель пользователя."""

    title = models.CharField(_("Title"), max_length=200, default="candidate")
    name = models.CharField(_("Name"), max_length=200)
    surname = models.CharField(_("Surname"), max_length=200)
    image = models.ImageField(
        _("Image"), upload_to="user_image/", blank=True, null=True
    )
    search_job_title = models.CharField(
        _("What job the candidate wants to find"),
        max_length=200,
        blank=True,
        null=True,
    )
    email = models.EmailField("Email", max_length=254, unique=True)
    distant_work = models.BooleanField(_("Ready for remote job"), default=True)
    phone_num = models.CharField(
        _("Phone number"), max_length=12, blank=True, null=True
    )
    city = models.CharField(_("City"), max_length=200, blank=True, null=True)
    country = models.CharField(
        _("Country"), max_length=200, blank=True, null=True
    )
    about = models.TextField(_("About candidate"), blank=True, null=True)
    about_skills = models.TextField(
        _("About candidate's skills"), blank=True, null=True
    )
    telegram = models.URLField(_("Telegram link"), blank=True, null=True)
    linkedin = models.URLField(_("Linkedin link"), blank=True, null=True)
    github = models.URLField(_("Github link"), blank=True, null=True)
    stack_overflow = models.URLField(
        _("Stack Overflow link"), blank=True, null=True
    )
    codeopen = models.URLField(_("Codeopen link"), blank=True, null=True)

    is_chosen_candidate = models.BooleanField(
        _("Chosen candidate"),
        default=True,
    )

    class Meta:
        constraints = [
            models.constraints.UniqueConstraint(
                fields=["is_chosen_candidate"],
                condition=Q(is_chosen_candidate=True),
                name="unique_is_chosen_candidate",
            )
        ]

    def __str__(self):
        return f"{self.name} {self.surname} - {self.title}"


class Job(models.Model):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="jobs",
    )
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    company = models.CharField(_("Company name"), max_length=200)
    company_link = models.URLField(_("Company's website url"))
    date_from = models.DateField(_("Date from"))
    date_to = models.DateField(_("Date to"), blank=True, null=True)

    class Meta:
        ordering = ("-date_from",)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    percent = models.PositiveSmallIntegerField(
        _("Percentage"),
        validators=[MaxValueValidator(100), MinValueValidator(1)],
    )

    class Meta:
        ordering = ("-percent",)
        abstract = True

    def __str__(self):
        return self.title


class HardSkill(Skill):
    class Level(models.TextChoices):
        GOOD = "Good", _("Good")
        ADVANCED = "Advanced", _("Advanced")
        EXPERT = "Expert", _("Expert")
        PRO = "Pro", _("Pro")

    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="hard_skills",
    )
    level = models.CharField(_("Level"), max_length=100, choices=Level.choices)

    class Meta(Skill.Meta):
        abstract = False


class SoftSkill(Skill):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="soft_skills",
    )

    class Meta(Skill.Meta):
        abstract = False


class Education(models.Model):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="educations",
    )
    title = models.CharField(_("Title"), max_length=200)
    place = models.CharField(_("Institution name"), max_length=200)
    date_from = models.DateField(_("Date from"))
    date_to = models.DateField(_("Date to"), blank=True, null=True)
    image = models.FileField(
        _("Certificate"), upload_to="certificate/", blank=True, null=True
    )

    def __str__(self):
        return self.title


class Language(models.Model):
    class Stars(models.TextChoices):
        ONE = "0", _("One star")
        TWO = "01", _("Two stars")
        THREE = "012", _("Three stars")
        FOUR = "0123", _("Four stars")
        FIVE = "01234", _("Five stars")

    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="languages",
    )
    title = models.CharField(_("Title"), max_length=200)
    level = models.CharField(_("Level"), max_length=200)
    stars = models.CharField(_("Extent"), max_length=5, choices=Stars.choices)

    def __str__(self):
        return self.title


class Recomendation(models.Model):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="recomendations",
    )
    text = models.TextField(_("Text"))
    author = models.CharField(_("Author"), max_length=200)
    author_job_title = models.CharField(
        _("Author's job title"), max_length=200
    )

    def __str__(self):
        return self.author


class OtherProject(models.Model):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="other_projects",
    )
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    github_link = models.URLField(_("Github link"))
    finish_date = models.DateField(_("Project end date"))

    class Meta:
        ordering = ("-finish_date",)

    def __str__(self):
        return self.title


class Project(models.Model):
    candidate = models.ManyToManyField(
        Candidate,
        verbose_name=_("Candidate"),
        related_name="projects",
    )
    image = models.ImageField(_("Preview"), upload_to="previews/")
    online_link = models.URLField(_("Link"))
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(
        _("Description"),
        help_text=_(
            "General description in one sentence, key goal, "
            "what you've implemented in the project. 3-4 santances"
        ),
    )
    github_link = models.URLField(_("Github link"))
    finish_date = models.DateField(_("Project end date"))
    stack = models.ManyToManyField(
        "Stack",
        verbose_name=_("Stack"),
        related_name="projects",
    )

    class Meta:
        ordering = ("-finish_date",)

    def __str__(self):
        return self.title


class File(models.Model):
    """
    Model for storing candidates files such as CV
    or something of that kind.
    """

    candidate = models.ForeignKey(
        Candidate,
        verbose_name=_("Candidate"),
        on_delete=models.CASCADE,
        related_name="files",
    )
    image = models.FileField(
        _("File"),
        upload_to="files/",
    )
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"), blank=True, null=True)
    change_date = models.DateTimeField(_("Change date"), auto_now=True)

    class Meta:
        ordering = ("-change_date",)

    def __str__(self):
        return self.title


class Stack(models.Model):
    title = models.CharField(_("Title"), max_length=30, unique=True)

    def __str__(self) -> str:
        return self.title
