"""Sets up URL files for all applications in this project."""

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), # load login/registration page
    url(r'^login$', views.login), # validate and login a user
    url(r'^logout$', views.logout), # logout a user
    url(r'^dashboard$', views.get_dashboard_data), # fetch dashboard data and load dashboard
]
