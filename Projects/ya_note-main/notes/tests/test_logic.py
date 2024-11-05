from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from notes.forms import WARNING
from notes.models import Note


User = get_user_model()


class TestNoteCreation(TestCase):
    TITLE = 'Заголовок'
    TEXT = 'Текст'

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Автор')
        cls.auth_client = Client()
        cls.auth_client.force_login(cls.user)
        cls.url = reverse('notes:add')
        cls.form_data = {
            'title': cls.TITLE,
            'text': cls.TEXT,
            'author': cls.auth_client
        }

    def test_user_can_add_note(self):
        self.auth_client.post(self.url, data=self.form_data)
        note_count = Note.objects.count()
        self.assertEqual(note_count, 1)
        note = Note.objects.get()
        self.assertEqual(note.title, self.TITLE)
        self.assertEqual(note.text, self.TEXT)
        self.assertEqual(note.author, self.user)

    def test_anonymous_user_cant_add_note(self):
        self.client.post(self.url, self.form_data)
        note_count = Note.objects.count()
        self.assertEqual(note_count, 0)

    def test_user_cant_add_with_existing_slug(self):
        Note.objects.create(
            title=self.TITLE,
            text=self.TEXT,
            author=self.user)
        note = Note.objects.get()
        response = self.auth_client.post(self.url, data=self.form_data)
        self.assertFormError(
            response,
            form='form',
            field='slug',
            errors=note.slug + WARNING
        )
        note_count = Note.objects.count()
        self.assertEqual(note_count, 1)


class TestNoteEditDetailDelete(TestCase):
    TITLE = 'Заголовок'
    TEXT = 'Текст'
    NEW_TEXT = 'Новый текст'

    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create(username='Автор')
        cls.author_client = Client()
        cls.author_client.force_login(cls.author)

        cls.other_user = User.objects.create(username='Другой пользователь')
        cls.other_user_client = Client()
        cls.other_user_client.force_login(cls.other_user)

        cls.note = Note.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
            author=cls.author,
        )

        cls.edit_url = reverse('notes:edit', args=(cls.note.slug,))
        cls.detail_url = reverse('notes:detail', args=(cls.note.slug,))
        cls.delete_url = reverse('notes:delete', args=(cls.note.slug,))
        cls.url_to_done = reverse('notes:success')

        cls.form_data = {
            'title': cls.TITLE,
            'text': cls.NEW_TEXT,
        }

    def test_author_can_edit_note(self):
        response = self.author_client.post(self.edit_url, data=self.form_data)
        self.assertRedirects(response, self.url_to_done)
        self.note.refresh_from_db()
        self.assertEqual(self.note.text, self.NEW_TEXT)

    def test_user_cant_edit_note(self):
        response = self.other_user_client.post(
            self.edit_url, data=self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.note.refresh_from_db()
        self.assertEqual(self.note.text, self.TEXT)

    def test_author_can_check_note_detail(self):
        response = self.author_client.get(self.detail_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_cant_check_note_detail(self):
        response = self.other_user_client.get(self.detail_url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_author_can_delete_note(self):
        response = self.author_client.delete(self.delete_url)
        self.assertRedirects(response, self.url_to_done)
        note_count = Note.objects.count()
        self.assertEqual(note_count, 0)

    def test_user_cant_delete_note(self):
        response = self.other_user_client.delete(self.delete_url)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        note_count = Note.objects.count()
        self.assertEqual(note_count, 1)
