from django.db import models

from wordpress_db import WORDPRESS_PT_USER_TABLE

class WpPtUserDatabase(models.Model):
    """ Model of the pasteque table in wordpress database.
    This table maps WordPress users their pasteque database.
    This model is obviously unmanaged by django's migration system.
    """
    user_id = models.BigIntegerField(primary_key=True, db_column='user_id')
    host = models.CharField(max_length=52, null=False, db_column='host')
    port = models.IntegerField(null=False, db_column='port')
    database = models.CharField(max_length=100, null=False, db_column='database')
    user = models.CharField(max_length=100, null=False, db_column='user')
    password = models.CharField(max_length=100, null=False, db_column='password')

    class Meta:
        db_table = WORDPRESS_PT_USER_TABLE
        managed = False
