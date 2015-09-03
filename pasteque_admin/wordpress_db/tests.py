from django.test import TestCase
from django.utils import timezone

from wordpress_auth_lite.models import WpUsers
from wordpress_db.models import WpPtUserDatabase
from wordpress_db.utils import get_pt_user_database


class UtilsTestCase(TestCase):
    """ Test functions in wordpress_db.utils """

    def setUp(self):
        WpUsers.objects.using('wordpress').create(
            id=3, login='poutine', password='1234', nicename='poutine',
            email='poutine@gov.ru', url='poutine.gov.ru',
            user_registered=timezone.now(),
            user_activation_key='', user_status=0, display_name='poutine'
        )

        WpPtUserDatabase.objects.using('wordpress').create(
            user_id=3, host='localhost', port='4242',
            database='foo', user='poutine', password='tinepou'
        )

    def tearDown(self):
        WpUsers.objects.using('wordpress').get(id=3).delete()
        WpPtUserDatabase.objects.using('wordpress').get(user_id=3).delete()

    def test_get_pt_user_database(self):
        wp_user = WpUsers.objects.using('wordpress').get(id=3)
        self.assertIsNotNone(wp_user)
        pt_user = get_pt_user_database(wp_user)
        self.assertIsNotNone(wp_user)
        self.assertEqual(pt_user.user, 'poutine')
