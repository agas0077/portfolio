from django.db import models


class Candidate(models.Model):
    """Модель пользователя."""

    name = models.CharField('Имя', max_length=200)
    surname = models.CharField('Фамилия', max_length=200)
    image = models.ImageField('Фотография', upload_to='user_image/',
                              blank=True, null=True)
    search_job_title = models.CharField(
        'Какую работу ищу', max_length=200, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    distant_work = models.BooleanField(
        'Готовность к удаленной работе', default=True)
    phone_num = models.CharField(
        'Номер телефона', max_length=12, blank=True, null=True)
    city = models.CharField('Город', max_length=200, blank=True, null=True)
    country = models.CharField('Страна', max_length=200, blank=True, null=True)
    about = models.TextField('О себе', blank=True, null=True)
    telegram = models.URLField('Ссылка на Telegram', blank=True, null=True)
    linkedin = models.URLField('Ссылка на Linkedin', blank=True, null=True)
    github = models.URLField('Ссылка на Github', blank=True, null=True)
    stack_overflow = models.URLField(
        'Ссылка на Stack Overflow', blank=True, null=True)
    codeopen = models.URLField('Ссылка на Codeopen', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Job(models.Model):
    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='jobs')
    title = models.CharField('Должность', max_length=200)
    description = models.TextField('Описание')
    company = models.CharField('Названи компании', max_length=200)
    company_link = models.URLField('Ссылка на сайт компании')
    date_from = models.DateField('Начало работы')
    date_to = models.DateField('Окончание работы', blank=True, null=True)

    class Meta:
        ordering = ('-date_from',)

    def __str__(self):
        return self.title


class Skill(models.Model):
    class Level(models.TextChoices):
        GOOD = 'Good', 'Хорошее владение'
        ADVANCED = 'Advanced', 'Продвинутое владение'
        EXPERT = 'Expert', 'Экспертное владение'
        PRO = 'Pro', 'Профессиональное владение'

    class Percent(models.IntegerChoices):
        GOOD = 80, 'Хорошее владение'
        ADVANCED = 85, 'Продвинутое владение'
        EXPERT = 90, 'Экспертное владение'
        PRO = 95, 'Профессиональное владение'

    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='skills')
    title = models.CharField('Название', max_length=200)
    tooltip = models.CharField('Подсказка', max_length=100)
    level = models.CharField('Степень', max_length=100, choices=Level.choices)
    percent = models.IntegerField('Процент владения', choices=Percent.choices)

    def __str__(self):
        return self.title


class Education(models.Model):
    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='educations')
    title = models.CharField('Название', max_length=200)
    place = models.CharField('Учебное заведение', max_length=200)
    date_from = models.DateField('Начало обучения')
    date_to = models.DateField('Окончание обучения', blank=True, null=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    class Stars(models.TextChoices):
        ONE = '0', 'Одна звезда'
        TWO = '01', 'Две звезды'
        THREE = '012', 'Три звезды'
        FOUR = '0123', 'Четыре звезды'
        FIVE = '01234', 'Пять звезд'

    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='languages')
    title = models.CharField('Название', max_length=200)
    level = models.CharField('Уровень владения', max_length=200)
    stars = models.CharField(
        'Степень владения', max_length=5, choices=Stars.choices)

    def __str__(self):
        return self.title


class Recomendation(models.Model):
    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='recomendations')
    text = models.TextField('Текст рекомендации')
    author = models.CharField('Автор рекомендации', max_length=200)
    author_job_title = models.CharField('Должность автора рекомендации',
                                        max_length=200)

    def __str__(self):
        return self.author


class OtherProject(models.Model):
    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='other_projects')
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    github_link = models.URLField('Ссылка на GitHub')
    finish_date = models.DateField('Дата завершения проекта')

    class Meta:
        ordering = ('-finish_date', )

    def __str__(self):
        return self.title


class Project(models.Model):
    user = models.ForeignKey(Candidate,
                             on_delete=models.CASCADE,
                             related_name='projects')
    image = models.ImageField('Превью', upload_to='previews/')
    online_link = models.URLField('Ссылка на проект')
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    github_link = models.URLField('Ссылка на GitHub')
    finish_date = models.DateField('Дата завершения проекта')

    class Meta:
        ordering = ('-finish_date', )

    def __str__(self):
        return self.title
