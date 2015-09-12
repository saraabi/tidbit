from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'tidbit.views.home_page', name='home'),
    url(r'^lists/the-only-story-in-the-world/$', 'tidbit.views.view_list', name='view_list'),
    url(r'^lists/new$', 'tidbit.views.new_list', name='new_list'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
]
