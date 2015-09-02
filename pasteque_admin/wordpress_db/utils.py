from wordpress_db.models import WpPtUserDatabase
from wordpress_auth_lite.models import WpUsers

def getPtUserDatabase(wpUser):
    try:
        return WpPtUserDatabase.objects.using('wordpress')\
            .get(user_id=wpUser.id)
    except WpPtUserDatabase.DoesNotExist:
        return None
