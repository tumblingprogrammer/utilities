from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^slugifier/$', views.slugifier, name='slugifier'),
    url(r'^django-secret-key-generator/$', views.django_secret_key_generator, name='django_secret_key_generator'),
    url(r'^accounts/profile/$', views.profile, name='profile'),

]