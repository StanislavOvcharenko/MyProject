from django.urls import reverse


def test_api_car_story_list(api_client):
    response = api_client.get(reverse('api:car_stories', kwargs={'vin_code': '12345678901234567'}))
    assert response.status_code == 200
    assert len(response.json()) == 12


def test_api_service_station_details(api_client):
    response = api_client.get(reverse('api:service_station_details', kwargs={'pk': '2'}))
    assert response.status_code == 200
    assert response.json() == {'station_name': 'Моя Станція2', 'city': 'Дніпро', 'address': 'Кутузова',
                               'phone': '0999999', 'email': 'admin1@admin.com',
                               'station_avatar': 'http://testserver/media/accounts/images/default_station_photo.jpeg'}


def test_api_service_stations_rating_list(api_client):
    response = api_client.get(reverse('api:service_station_rating_list'))
    assert response.status_code == 200
    assert len(response.json()) == 6
