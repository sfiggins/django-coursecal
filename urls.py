from django.conf.urls.defaults import *
from coursecal.models import Course

info_dict = {
    'queryset': Course.objects.all(),
}


urlpatterns = patterns(
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
)

urlpatterns += patterns('coursecal.views',
    (r'^calendar/$', 'event_calendar'),
    (r'^detail/(?P<slug_id>[0-9A-Za-z-]+)/$', 'course_by_slug'),
)


