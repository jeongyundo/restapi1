from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
]
#r'^ ~~ ' 를 사용해야 리스트안으로 들어가야 다른 패턴에 사용가능하다.

urlpatterns = format_suffix_patterns(urlpatterns)