from django.db import models


class HowWorks(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name = 'كيف نعمل'
        verbose_name_plural = 'كيف نعمل'

    def __str__(self):
        return self.title
