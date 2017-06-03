from django.conf.urls import url, include
from django.contrib import admin
from manage import get_env_variable
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
]

DJANGO_EXECUTION_ENVIRONMENT = get_env_variable('DJANGO_EXECUTION_ENVIRONMENT')
if DJANGO_EXECUTION_ENVIRONMENT == 'LOCAL':
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)