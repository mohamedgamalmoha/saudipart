from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.backends import get_user_model


User = get_user_model()

NationalIDValidator = RegexValidator(r'^[0-9]*', 'Only digit characters.')
PhoneNumberValidator = RegexValidator(r'^[0-9]{10}', 'Only digit characters.')


TRANSFORMATION_TYPES = (
    ('direct', 'مباشرة'),
    ('mediator', 'عبر وسيط'),
)


class Robbery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    victim_name = models.CharField('اسم الضحية', max_length=50)
    victim_national_id = models.CharField('رقم البطاقه الوطنيه لضحية', max_length=11, validators=[NationalIDValidator])
    victim_phone_number = models.CharField('رقم جوال الضحية', max_length=11, validators=[PhoneNumberValidator])
    embezzled_amount = models.DecimalField('المبلغ الذي تمت سرقته من الضحية', decimal_places=2, max_digits=20)
    outboard_transferred = models.CharField('هل تم التحويل للخارج مباشره', choices=TRANSFORMATION_TYPES, max_length=50)
    mediator_iban = models.CharField('اي بان الوسيط', blank=True, null=True, max_length=150)
    gang_iban = models.CharField('اي بان العصابة', max_length=150)

    class Meta:
        verbose_name = 'الضحية'
        verbose_name_plural = 'الضحية'

    def __str__(self):
        return self.victim_name

    @property
    def is_transferred(self):
        return self.outboard_transferred == 'direct'
