from django.db import models
from django.shortcuts import reverse


class Thief(models.Model):
    name = models.CharField(max_length=50, unique=True)
    ip_number = models.GenericIPAddressField(unique=True)

    class Meta:
        verbose_name = 'Thief'
        verbose_name_plural = 'Thief'

    def __str__(self):
        return self.ip_number

    def get_absolute_url(self):
        return reverse('thief:thief_profile', self.pk)


class Victim(models.Model):
    thief = models.ForeignKey(Thief, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    ip_number = models.GenericIPAddressField()
    embezzled_amount = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name = 'Victim'
        verbose_name_plural = 'Victim'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thief:victim_profile', self.pk)
