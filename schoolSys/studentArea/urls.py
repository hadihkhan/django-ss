from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cust_login, name="cust_login")
]
