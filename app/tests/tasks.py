from autohistory.tasks import send_activate_mail
from accounts.models import User
from comments_and_rating.tasks import update_service_stations_rating



def test_send_activate__mail(mailoutbox):
    user = User.objects.get(pk=3)

    send_activate_mail(user.username, user.email)

    assert len(mailoutbox) == 1
    assert mailoutbox[
               0].body == '\n            Активація акакаунту: http://localhost:8000/' \
                          'accounts/activate/89266155-acf0-4f9a-9b12-7613f35dcf51/'


def test_update_service_stations_rating():
    update_service_stations_rating()
