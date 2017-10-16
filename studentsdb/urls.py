from django.conf.urls import patterns, include, url
from django.contrib import admin

from .settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static

from students.views.students import StudentUpdateView


urlpatterns = patterns('',
    #Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add',
         name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
         StudentUpdateView.as_view(),
         name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$',
         'students.views.students.students_delete',
         name='students_delete'),

    #Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add',
         name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$',
         'students.views.groups.groups_edit',
         name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$',
         'students.views.groups.groups_delete',
         name='groups_delete'),

    #Journal urls
    url(r'^journal/$', 'students.views.journal.journal_list', name='journal'),
    url(r'^journal/(?P<sid>\d+)$', 'students.views.journal.journal_student',
        name='journal_student'),
    url(r'^journal/update/$', 'students.views.journal.journal_update',
        name='journal_update'),

    #Exams urls
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^exams/add$', 'students.views.exams.exams_add', name='exams_add'),
    url(r'^exams/result/(?P<gid>\d+)/$',
        'students.views.exams.exams_result', name='exams_result'),

    #Contact admin form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
        name='contact_admin'),

    url(r'^admin/', include(admin.site.urls)),

)

if DEBUG:
    # serve files from media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
