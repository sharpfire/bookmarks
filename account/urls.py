from django.conf.urls import url
from account.views import user_login

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
]