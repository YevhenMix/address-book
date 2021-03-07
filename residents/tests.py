from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import Q
from django.test import TestCase, Client
from django.urls import reverse
from residents.models import Resident


class TestMainView(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        photo = SimpleUploadedFile('photo.jpg', content=b'', content_type='image/jpg')
        self.resident = Resident.objects.create(
            first_name='Евгений',
            last_name='Михайлов',
            country='Украина',
            city='Запорожье',
            street='Мира',
            url='https://github.com/',
            phone_number='+380964225642',
            photo=photo
        )

    def test_main_view_get(self):
        response = self.client.get(reverse('residents:main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'residents/main.html')

    def test_main_view_post(self):
        response = self.client.post(reverse('residents:main'), {
            'search': 'ха'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'residents/main.html')

    def test_create_view(self):
        response = self.client.get(reverse('residents:create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'residents/create.html')

    def test_update_view(self):
        url = reverse('residents:update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'residents/update.html')

    def test_delete_view(self):
        url = reverse('residents:delete', kwargs={'pk': 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.client, Resident.objects.all())

    def test_create_resident(self):
        self.assertIn(self.resident, Resident.objects.all())


