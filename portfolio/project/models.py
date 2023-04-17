from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class OtherProject(models.Model):
    user = models.ForeignKey(User,
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
    user = models.ForeignKey(User,
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
