from django.urls import reverse
import pytest


def test_comments_and_rating_create_get(client):
    response = client.post(reverse('comments_and_rating:create_comments_and_rating', kwargs={'check_number': 12}))
    assert response.status_code == 200


def test_comments_and_rating_create_post_empty(client):
    response = client.post(reverse('comments_and_rating:create_comments_and_rating', kwargs={'check_number': 12}),
                           data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'rating': ['This field is required.'],
                                                    'comment_text': ['This field is required.']}


def test_comments_and_rating_create_valid_post(client):
    data = {'rating': 5.0,
            'comment_text': 'Good job!'}
    response = client.post(reverse('comments_and_rating:create_comments_and_rating', kwargs={'check_number': 12}),
                      data=data)
    assert response.status_code == 302
    assert response.url == '/'


def test_test_comments_and_rating_create_invalid_check_number_get(client):
    response = client.get(reverse('comments_and_rating:create_comments_and_rating', kwargs={'check_number': 2222}))
    assert response.status_code == 404


@pytest.mark.parametrize('rating', ['ssss', 0, -1, 6])
def test_comments_and_rating_create_invalid_post_invalid_rating_field(client, rating):
    data = {'rating': rating,
            'comment_text': 'Good job!'}
    response = client.post(reverse('comments_and_rating:create_comments_and_rating', kwargs={'check_number': 12}),
                           data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'rating': ['Enter a whole number.']}


def test_service_station_rating_list_get(client):
    response = client.get(reverse('comments_and_rating:service_stations_rating'))
    assert response.status_code == 200


def test_service_station_rating_list_get_page(client):
    response = client.get(f'{reverse("comments_and_rating:service_stations_rating")}?page=2')
    assert response.status_code == 200
