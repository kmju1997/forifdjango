from django.conf.urls import url
from . import views

app_name = 'musicapp'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r"^(?P<album_id>[0-9]+)/favorite/$", views.favorite, name="favorite"),
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add')
]