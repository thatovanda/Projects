from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^$', index, name="index"),
    #127.0.0.1/polls/
    url(r'^(?P<question_id>[0-9]+)/$', detail, name="detail"),
    #127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/results$', results, name="results"),
    #127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/vote$', vote, name="vote"),
    #127.0.0.1/polls/1/vote

    url(r'^display_company$', display_company, name="display_company"),
    url(r'^register_company$', register_company, name="register_company"),
    url(r'^edit_company$', edit_company, name="edit_company"),
]

app_name="polls"
