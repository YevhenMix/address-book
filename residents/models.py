from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Resident(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    country = models.CharField(max_length=57)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    url = models.URLField()
    phone_number = PhoneNumberField(unique=True)
    photo = models.ImageField(upload_to='static/image')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Житель'
        verbose_name_plural = 'Жители'
        unique_together = ('first_name', 'last_name')
        ordering = ['first_name']
