from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^slugifier/$', views.slugifier, name='slugifier'),
    url(r'^accounts/profile/$', views.profile, name='profile'),

]