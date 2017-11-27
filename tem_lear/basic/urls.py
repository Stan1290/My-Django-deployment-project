from django.conf.urls import url
from basic import views



app_name = 'basic'


urlpatterns = [


    url(r'^other/', views.other, name = 'other' ),
    url(r'^rel_template/', views.rel_template_url, name = 'rel_template' ),
    url(r'^registrate/', views.registrate, name = 'registrate'),
    url(r'^secret/$', views.check_if_logged_in, name = 'secret'),


]
