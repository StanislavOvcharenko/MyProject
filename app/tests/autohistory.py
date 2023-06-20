

from django.urls import reverse
import pytest
from accounts.models import ServiceStation, User



def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_post_empty(client):
    response = client.post('/', data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'vin': ['This field is required.']}


def test_index_post_valid(client):
    response = client.post('/', data={'vin': '12345678901234567'})
    assert response.status_code == 302
    assert response.url == '/autohistory/car-story/list/12345678901234567/'


@pytest.mark.parametrize('vin_code', ('123456789012345670', '2', 'qqweqewqeqwe'))
def test_index_post_invalid(client, vin_code):
    response = client.post('/', data={'vin': vin_code})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'vin': [f'Ensure this value has at'
                                                            f' most 17 characters (it has {len(vin_code)}).']} or \
           {'vin': [f'Ensure this value has at least 17 characters (it has {len(vin_code)}).']}


def test_car_story_get_valid(client):
    response = client.get(reverse('autohistory:car_story', kwargs={'pk': '12345678901234567'}))
    assert response.status_code == 200
    assert len(response.context_data['object_list']) == 5


def test_car_story_get_page(client):
    response = client.get(f'{reverse("autohistory:car_story", kwargs={"pk": "12345678901234567"})}?page=2')
    assert response.status_code == 200


def test_create_autohistory_get(client):
    response = client.get(reverse('autohistory:create_auto_history'))
    assert response.status_code == 200


def test_create_autohistory_post_empty(client):
    response = client.post(reverse('autohistory:create_auto_history'), data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'vin_code': ['This field is required.'],
                                                    'mileage_units': ['This field is required.'],
                                                    'mileage': ['This field is required.'],
                                                    'mileage_photo': ['This field is required.'],
                                                    'service_station_name': ['This field is required.'],
                                                    'damage': ['This field is required.'],
                                                    'work': ['This field is required.'],
                                                    'check_number': ['This field is required.'],
                                                    'email': ['This field is required.']
                                                    }


def test_create_autohistory_post_valid(client, load_image, mailoutbox):
    a = ServiceStation.objects.get(id=2)
    user = User.objects.get(pk=3)
    client.force_login(user)
    data = {'vin_code': '12345678901234567',
            'mileage_units': 'Км',
            'mileage': 200,
            'mileage_photo': load_image,
            'service_station_name': str(a.id),
            'damage': 'any',
            'work': 'any',
            'check_number': '12345678',
            'email': 'admin@admin.com',
            }
    response = client.post(reverse('autohistory:create_auto_history'), data=data)
    assert response.status_code == 302
    assert response.url == '/'
    assert len(mailoutbox) == 1


def test_test_create_autohistory_post_invalid_email(client, load_image):

    a = ServiceStation.objects.get(id=2)
    user = User.objects.get(pk=3)
    client.force_login(user)
    data = {'vin_code': '12345678901234567',
            'mileage_units': 'Км',
            'mileage': 200,
            'mileage_photo': load_image,
            'service_station_name': str(a.id),
            'damage': 'any',
            'work': 'any',
            'check_number': '12345678',
            'email': 'adminadmin.com',
            }
    response = client.post(reverse('autohistory:create_auto_history'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}


def test_create_autohistory_post_wrong_mileage_units(client, load_image):
    a = ServiceStation.objects.get(id=2)
    user = User.objects.get(pk=3)
    client.force_login(user)
    data = {'vin_code': '12345678901234567',
            'mileage_units': 'kk',
            'mileage': 200,
            'mileage_photo': load_image,
            'service_station_name': str(a.id),
            'damage': 'any',
            'work': 'any',
            'check_number': '12345678',
            'email': 'admin@admin.com',
            }
    response = client.post(reverse('autohistory:create_auto_history'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'mileage_units':
                                                       ['Select a valid choice.'
                                                        ' kk is not one of the available choices.']}


def test_details_autohistory_get(client):
    response = client.get(reverse('autohistory:history_details', kwargs={'pk': '3'}))
    assert response.status_code == 200


def test_details_autohitory_get_invalid_pk(client):
    response = client.get(reverse('autohistory:history_details', kwargs={'pk': '22'}))
    assert response.status_code == 404


def test_car_story_damage_photos_get(client):
    response = client.get(reverse('autohistory:damage_photos', kwargs={'pk': 5}))
    assert response.status_code == 200


