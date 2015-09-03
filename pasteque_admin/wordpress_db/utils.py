from wordpress_db.models import WpPtUserDatabase
from wordpress_auth_lite.models import WpUsers

def get_pt_user_database(wpUser):
    """ Takes a WpUsers and returns the WpPtUserDatabase associated """
    try:
        return WpPtUserDatabase.objects.using('wordpress')\
            .get(user_id=wpUser.id)
    except WpPtUserDatabase.DoesNotExist:
        return None
