from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rail import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^train/', include('rail.urls')),
    url(r'^', include('rail.urls')),
    url(r'^vonatjson', views.AlbumList.as_view(),name='vonatjson'),
    url(r'^vpejson', views.VpeList.as_view()),
    url(r'^mozdonyjson', views.MozdonyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)