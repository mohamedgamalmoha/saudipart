from django.db import models


class HowWorks(models.Model):
    title = models.CharField('عنوان',  max_length=250)
    description = models.TextField('وصف')

    class Meta:
        verbose_name = 'كيف نعمل'
        verbose_name_plural = 'كيف نعمل'

    def __str__(self):
        return self.title
