import pytest
from django.test.client import Client
from news.models import News, Comment


@pytest.fixture
def news():
    news = News.objects.create(title='Заголовок', text='Текст')
    return news


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def not_author(django_user_model):
    return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def not_author_client(not_author):
    client = Client()
    client.force_login(not_author)
    return client


@pytest.fixture
def comment(author, news):
    return Comment.objects.create(
        news=news,
        author=author,
        text='Текст комментария',
    )


@pytest.fixture
def id_for_args(news):
    return (news.id,)


@pytest.fixture
def comment_pk_for_args(comment):
    return (comment.pk,)
