from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from notes.models import Note


User = get_user_model()


class TestListPage(TestCase):
    NUMBER_NOTES = 5

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор')
        cls.other_client = User.objects.create(username='Другой клиент')
        for index in range(cls.NUMBER_NOTES):
            Note.objects.create(
                title=f'Заметка {index}',
                text='Текст',
                author=cls.author
            )

    def test_notes_count(self):
        users_counts = (
            (self.author, self.NUMBER_NOTES),
            (self.other_client, 0),
        )

        for client, count in users_counts:
            with self.subTest(client=client, count=count):
                url = reverse('notes:list')
                self.client.force_login(client)
                response = self.client.get(url)
                all_notes = response.context['object_list']
                new_count = all_notes.count()
                self.assertEqual(new_count, count)



