from django.urls import reverse


def test_signup_get(client):
    response = client.get(reverse('accounts:signup'))
    assert response.status_code == 200


def test_signup_post_empty(client):
    response = client.post(reverse('accounts:signup'), data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['This field is required.'],
                                                    'password': ['This field is required.'],
                                                    'password_confirmation': ['This field is required.']}


def test_signup_post_valid_data(client, mailoutbox):
    data = {'email': 'admin@example.com',
            'password': 'admin@example.com',
            'password_confirmation': 'admin@example.com'}
    response = client.post(reverse('accounts:signup'), data=data)
    assert response.status_code == 302
    assert response.url == '/accounts/auth/login/'
    assert len(mailoutbox) == 1


def test_signup_post_invalid_email(client):
    data = {'email': 'adminexample.com',
            'password': 'admin@example.com',
            'password_confirmation': 'admin@example.com'}
    response = client.post(reverse('accounts:signup'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}


def test_signup_post_invalid_password(client):
    data = {'email': 'admin@example.com',
            'password': 'adminexample.com',
            'password_confirmation': 'admin@example.com'}
    response = client.post(reverse('accounts:signup'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'__all__': ['Паролі не співпадають']}


def test_profile_get(logged_user):
    response = logged_user.get(reverse('accounts:profile'))
    assert response.status_code == 200


def test_profile_post_empty(logged_user):
    response = logged_user.post(reverse('accounts:profile'), data={})
    assert response.context_data['form'].errors == {'EDRPOU': ['This field is required.'],
                                                    'company_name': ['This field is required.']}
    assert response.status_code == 200


def test_profile_post_valid_data(logged_user):
    data = {'EDRPOU': '9999999',
            'company_name': '456456456'}
    response = logged_user.post(reverse('accounts:profile'), data=data)
    assert response.status_code == 302


def test_create_service_station_get(logged_user):
    response = logged_user.get(reverse('accounts:create_service_station'))
    assert response.status_code == 200


def test_create_service_station_post_empty(logged_user):
    response = logged_user.post(reverse('accounts:create_service_station'), data={})
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'station_name': ['This field is required.'],
                                                    'city': ['This field is required.'],
                                                    'address': ['This field is required.'],
                                                    'phone': ['This field is required.'],
                                                    'email': ['This field is required.'],
                                                    'company': ['This field is required.']}


def test_create_service_station_post_invalid_email(logged_user):
    data = {'station_name': 'my station',
            'city': 'Dnipro',
            'address': 'Dniprovska 2',
            'phone': '9379992',
            'email': 'testexample.com',
            'company': 3
            }

    response = logged_user.post(reverse('accounts:create_service_station'), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}


def test_create_service_station_post_valid_data(logged_user):
    data = {'station_name': 'my station',
            'city': 'Dnipro',
            'address': 'Dniprovska 2',
            'phone': '9379992',
            'email': 'test@example.com',
            'company': 3
            }
    response = logged_user.post(reverse('accounts:create_service_station'), data=data)
    assert response.status_code == 302


def test_service_station_list_get(logged_user):
    response = logged_user.get(reverse('accounts:list_service_station'))
    assert response.status_code == 200


def test_service_station_details_get(logged_user):
    response = logged_user.get(reverse('accounts:details_service_station', kwargs={'pk': 3}))
    assert response.status_code == 200


def test_service_station_details_get_invalid_pk(logged_user):
    response = logged_user.get(reverse('accounts:details_service_station', kwargs={'pk': 2222}))
    assert response.status_code == 404


def test_service_station_update_get(logged_user):
    response = logged_user.get(reverse('accounts:update_service_station', kwargs={'pk': 3}))
    assert response.status_code == 200


def test_service_station_update_post_empty(logged_user):
    response = logged_user.post(reverse('accounts:update_service_station', kwargs={'pk': 3}), data={})
    assert response.context_data['form'].errors == {'station_name': ['This field is required.'],
                                                    'city': ['This field is required.'],
                                                    'address': ['This field is required.'],
                                                    'phone': ['This field is required.'],
                                                    'email': ['This field is required.']}
    assert response.status_code == 200


def test_service_station_update_post_valid_data(logged_user):
    data = {'station_name': 'New station',
            'city': 'Dnipro',
            'address': 'Dnipro 3',
            'phone': '9379992',
            'email': 'test@example.com'}
    response = logged_user.post(reverse('accounts:update_service_station', kwargs={'pk': 3}), data=data)
    assert response.status_code == 302


def test_service_station_update_post_invalid_email(logged_user):
    data = {'station_name': 'New station',
            'city': 'Dnipro',
            'address': 'Dnipro 3',
            'phone': '9379992',
            'email': 'testexample.com'}
    response = logged_user.post(reverse('accounts:update_service_station', kwargs={'pk': 3}), data=data)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {'email': ['Enter a valid email address.']}


def test_activate_get(client):
    response = client.get(reverse('accounts:activate', kwargs={'username': '1cc500f1-def5-4c65-ba68-d720b39bfe7a'}))
    assert response.status_code == 302

