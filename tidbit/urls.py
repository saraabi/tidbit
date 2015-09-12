from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:

    url(r'^(\d+)/$', 'tidbit.views.view_list', name='view_list'),
    url(r'^(\d+)/add_item$', 'tidbit.views.add_item', name='add_item'),
    url(r'^new$', 'tidbit.views.new_list', name='new_list'),

]
