import datetime

from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required

from worklog.views import ReportView

DATEMIN = r'(?P<datemin>\d{4}-\d{2}-\d{2})'
DATEMAX = r'(?P<datemax>\d{4}-\d{2}-\d{2})'
# accepts:  date_date   or   date_   or   _date
DATERANGE1 = '(?:'+DATEMIN+'_'+DATEMAX+'?)'
DATERANGE2 = '(?:_'+DATEMAX+')'

USERNAME = r'(?P<username>[a-zA-Z0-9]+)'
##JOBID = r'(?:_job_(?P<jobid>[0-9]+))'

urlpatterns = patterns('worklog',
    (r'^add/$', 'views.createWorkItem', {'reminder_id': None}),
    (r'^add/reminder_(?P<reminder_id>[0-9a-f\-]{36})/$','views.createWorkItem', {}, 'worklog-reminder-view'), # last item is the view-name
    
    (r'^view/$', 'views.viewWork'),
    #(r'^view/today/$', 'views.viewWork', {'datemin': datetime.date.today(), 'datemax': datetime.date.today()}),
    (r'^view/today/$', 'views.viewWork', {'datemin': 'today', 'datemax': 'today'}),
    (r'^view/'+DATERANGE1+'/$', 'views.viewWork'),
    (r'^view/'+DATERANGE2+'/$', 'views.viewWork'),
    (r'^view/'+USERNAME+'/$', 'views.viewWork'),
    #(r'^view/'+USERNAME+'/today/$', 'views.viewWork', {'datemin': datetime.date.today(), 'datemax': datetime.date.today()}),
    (r'^view/'+USERNAME+'/today/$', 'views.viewWork', {'datemin': 'today', 'datemax': 'today'}),
    (r'^view/'+USERNAME+'/'+DATERANGE1+'/$', 'views.viewWork'),
    (r'^view/'+USERNAME+'/'+DATERANGE2+'/$', 'views.viewWork'),
)

urlpatterns += patterns('worklog',
    url(r'^view/report/(?P<date>\d{4}-\d{2}-\d{2})/$', login_required(ReportView.as_view()), name='report_url')
)