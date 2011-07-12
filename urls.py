from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/keiouu/nirtha/media', 'show_indexes': True}),
    
    (r'^login/$', 'core.views.login_view'),
    
    
    (r'^tasks/$', 'task.views.tasks_view'),
    (r'^tasks/(?P<id>.*)/$', 'task.views.task_view'),
    (r'^projects/$', 'project.views.projects_view'),
    (r'^projects/(?P<id>.*)/$', 'project.views.project_view'),
    
    #API
    (r'^api/tasks/create/$', 'task.views.tasks_new_view'),
    (r'^api/projects/create/$', 'project.views.projects_new_view'),
    (r'^$', 'core.views.index'),
)

# TODO:
# /logout/
# /profile/
# /profile/messages/

