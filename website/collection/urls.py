from django.conf.urls import url
from .views import (
    home_page,
    signup_page,
    login_page,
    logout_page,
    forget_password,

    account_page,
    my_space,
    professional_page,
    follower_page,
    following_page,
)


urlpatterns = [
    url(r'^$', home_page),
    url(r'^signup/$', signup_page),
    url(r'^logout/$', logout_page),
    url(r'^login/$', login_page),
    url(r'^forget_password/(?P<username>[\w.@+-]+)/(?:id-(?P<id>\d+)/)?$', forget_password),
    url(r'^account/$', account_page),
    url(r'^my-space/$', my_space),
    url(r'^professional_details/$', professional_page),
    url(r'^follower/$', follower_page),
    url(r'^following/$', following_page),
]
