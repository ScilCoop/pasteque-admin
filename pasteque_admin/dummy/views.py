from django.shortcuts import render
from django.http import HttpResponse

from wordpress_auth_lite.decorators import wordpress_login_required
from wordpress_db.utils import get_pt_user_database

from pasteque_db.database import Database, Credentials
from pasteque_db.models import Application, CashRegister


@wordpress_login_required
def dummy(request):
    pt_user_database = get_pt_user_database(request.wordpress_user)
    credentials = Credentials(
        driver='mysql',
        host=pt_user_database.host,
        port=pt_user_database.port,
        user=pt_user_database.user,
        password=pt_user_database.password,
        name=pt_user_database.name
    )
    database = Database(credentials.generate_sqla_url())

    session = database.new_session()

    application = session.query(Application).filter_by(id='pasteque').one()
    response = "<p>name: %s</p>" % application.name
    response += "<p>version: %s</p>" % application.version

    for loc in session.query(CashRegister).all():
        response += "<p>%s</p>" % str(loc.location.name)

    # response += "<p>Database = %s</p>" % database
    # response = "<p>Credentials = %s</p>" % credentials

    return HttpResponse(response)
