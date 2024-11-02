from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from news.models import News, Comment
from datetime import datetime, timedelta
from news.forms import CommentForm


User = get_user_model()


class TestHomePage(TestCase):
    HOME_URL = reverse('news:home')

    @classmethod
    def setUpTestData(cls):
        today = datetime.today()
        all_news = [
            News(title=f'Новость {index}', text='Просто текст', date=today - timedelta(days=index))
            for index in range(settings.NEWS_COUNT_ON_HOME_PAGE + 1)
        ]
        # Создание в БД сразу несколько записей
        News.objects.bulk_create(all_news)

    def test_news_count(self):
        response = self.client.get(self.HOME_URL)
        object_list = response.context['object_list']
        new_count = object_list.count()
        self.assertEqual(new_count, settings.NEWS_COUNT_ON_HOME_PAGE)

    def test_news_order(self):
        response = self.client.get(self.HOME_URL)
        object_list = response.context['object_list']
        all_date = [news.date for news in object_list]
        sorted_date = sorted(all_date, reverse=True)
        self.assertEqual(all_date, sorted_date)


class TestDetailPage(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(title='Заголовок', text='Текст')
        cls.detail_url = reverse('news:detail', args=(cls.news.pk,))
        cls.author = User.objects.create(username='Комментатор')
        now = timezone.now()
        for index in range(10):
            comment = Comment.objects.create(
                news=cls.news, author=cls.author, text=f'Текст {index}'
            )
            comment.created = now + timedelta(days=index)
            comment.save()

    def test_comment_order(self):
        response = self.client.get(self.detail_url)
        self.assertIn('news', response.context)
        news = response.context['news']
        all_comments = news.comment_set.all()
        all_timestamps = [comment.created for comment in all_comments]
        sorted_timestamps = sorted(all_timestamps)
        self.assertEqual(all_timestamps, sorted_timestamps)

    def test_anonymous_client_has_no_form(self):
        response = self.client.get(self.detail_url)
        self.assertNotIn('form', response.context)

    def test_authorized_client_has_form(self):
        self.client.force_login(self.author)
        response = self.client.get(self.detail_url)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], CommentForm)
