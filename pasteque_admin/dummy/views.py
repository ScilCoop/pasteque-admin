from django.shortcuts import render
from django.http import HttpResponse

from wordpress_auth_lite.decorators import wordpress_login_required

@wordpress_login_required
def dummy(request):
    return HttpResponse('<h1>hello world !</h1>')
