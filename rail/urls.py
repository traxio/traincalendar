from django.conf.urls import url
from . import views

app_name = 'rail'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index_creation_filter/$', views.index_creation_filter, name='index_creation_filter'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^vpes/(?P<filter_by>[a-zA_Z]+)/$', views.vpes, name='vpes'),
    url(r'^mozdonys/(?P<filter_by>[a-zA_Z]+)/$', views.mozdonys, name='mozdonys'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_vpe/$', views.create_vpe, name='create_vpe'),
    url(r'^(?P<album_id>[0-9]+)/create_mozdony/$', views.create_mozdony, name='create_mozdony'),
    url(r'^(?P<album_id>[0-9]+)/delete_vpe/(?P<vpe_id>[0-9]+)/$', views.delete_vpe, name='delete_vpe'),
    url(r'^(?P<album_id>[0-9]+)/update_vpe/(?P<vpe_id>[0-9]+)/$', views.update_vpe, name='update_vpe'),
    url(r'^(?P<album_id>[0-9]+)/view_vpe/(?P<vpe_id>[0-9]+)/$', views.view_vpe, name='view_vpe'),
    url(r'^(?P<album_id>[0-9]+)/delete_mozdony/(?P<mozdony_id>[0-9]+)/$', views.delete_mozdony, name='delete_mozdony'),
    url(r'^(?P<album_id>[0-9]+)/update_mozdony/(?P<mozdony_id>[0-9]+)/$', views.update_mozdony, name='update_mozdony'),
    url(r'^(?P<album_id>[0-9]+)/view_mozdony/(?P<mozdony_id>[0-9]+)/$', views.view_mozdony, name='view_mozdony'),
    #url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    url(r'^(?P<album_id>[0-9]+)/update_album/$', views.update_album, name='update_album'),
    url(r'^naptar/$', views.naptar, name='naptar'),
]
