from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"), # This is placed before the "detail" because we don't want to send "create" as a slug
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
