from django.conf.urls import url

from . import views

app_name = 'ajax_blog'
urlpatterns = [
    url(r'^$', views.index, name="index"),
]