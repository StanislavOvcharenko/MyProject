import pytest
# from rest_framework.test import APIClient
from django.core.management import call_command
from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import Client
from accounts.models import User


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'users.json',
            'servicestation.json',
            'carstory.json',
            'damagephoto.json',
            'commentsandratings.json',
            'servicestationrating.json',

        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')


@pytest.fixture(autouse=True, scope="function")
def load_image():
    img = SimpleUploadedFile(name='test_image.jpg', content=open('app/tests/fix_odometr.jpg', 'rb').read(),
                             content_type='image/jpeg')
    return img

@pytest.fixture
def logged_user(client):
    user = User.objects.get(pk=3)
    client.force_login(user)
    return client


