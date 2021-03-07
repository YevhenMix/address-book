from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Resident


class ResidentForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Введите ваше имя'}))

    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Введите вашу фамилию'}))

    country = forms.CharField(label='Страна',
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Введите вашу страну'}))

    city = forms.CharField(label='Город',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите ваш город'}))

    street = forms.CharField(label='Улица',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Введите вашу улицу'}))

    url = forms.URLField(label='Ссылка',
                         widget=forms.URLInput(attrs={'class': 'form-control',
                                                      'placeholder': 'Введите ссылку на ваш сайт'}))

    phone_number = PhoneNumberField(label='Номер телефона',
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите ваш номер телефона'}))

    photo = forms.ImageField(label='Фото',
                             widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Resident
        fields = ('first_name', 'last_name', 'country', 'city',
                  'street', 'url', 'phone_number', 'photo')


class SearchForm(forms.Form):
    search = forms.CharField(label='Поиск',
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Кого Вы ищите?',
                                                           'aria-label': "Recipient's username",
                                                           'aria-describedby': 'button-addon2'}))
