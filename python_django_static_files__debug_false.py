"""
this is not a runnable file,
but is very useful for those,
who are working with the
PYTHON/DJANGO framework.

here is an example code to
run your django app safely
in the production...
"""

## project's settings.py file

# somewhere near to the top of the file

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# so now, you have to set your allowed host(s)
ALLOWED_HOSTS = []
# for example: ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# at the bottom of the file

# Static files (CSS, JavaScript, Images)


STATIC_URL = "/static/"
MEDIA_URL = "/static/images/"

STATIC_ROOT = BASE_DIR / "assets"
MEDIA_ROOT =  BASE_DIR / "static/images"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# of course, you can give other names as well... this is just an example


## project's urls.py file

from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path('home/', include('home.urls')),
]



"""
so, that's it!
don't forget to run:
python manage.py collectstatic
(in this case, it will collect to the assets folder/directory)

and you don't have to use any third-party tools.
of those the well known and widely used:
whitenoise
"""
