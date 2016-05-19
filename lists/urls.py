from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^(\d+)/$', 'lists.views.view_list', name='view-list'),
    url(r'^new$', 'lists.views.new_list', name='new-list'),
)
