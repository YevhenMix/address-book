from django.contrib import admin

from .models import Resident


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'city',
                    'street', 'phone_number', 'url')
