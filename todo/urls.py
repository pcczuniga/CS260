from django.conf.urls import patterns, include, url
from app.views import home
from app.views import todo
from django.contrib import admin
import os.path

admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',url(r'^admin/', include(admin.site.urls)),)
urlpatterns += patterns('',(r'^$', home.main_page),)
urlpatterns += patterns('',(r'^signup$', home.signup),)
urlpatterns += patterns('',(r'^login$', home.login),)
urlpatterns += patterns('',(r'^logout$', home.logout),)
urlpatterns += patterns('',(r'^add-todo$', todo.add_todo),)
urlpatterns += patterns('',(r'^edit-todo/(?P<todo_id>\d+)$', todo.edit_todo),)
urlpatterns += patterns('',(r'^delete-todo/(?P<todo_id>\d+)$', todo.delete_todo),)
