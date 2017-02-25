from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseServerError
from django.http import HttpResponseForbidden
from watchdogesite.models import Report
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging

logger = logging.getLogger(__name__)

CHECK = hash('1337badwolf')

@csrf_exempt
def add(request):

    # Add new report
    if request.method == 'POST':
        params = request.content_params
        if (params.has_key('check') and params.has_key('type') and
            params.has_key('desc') and params.has_key('title') and
            params.has_key('pets') and params.has_key('entry')):
            if request.POST['check'] is not CHECK:
                return HttpResponseForbidden
            try:
                items = request.POST
                r = Report(type=items['type'], description=items['desc'], title=items['title'],
                           pets=items['pets'], entry=items['entry'])
                r.date = datetime.datetime.now().date()
                r.put()
            except Exception, e:
                return HttpResponseServerError('Failed to receive report')
            return HttpResponse(r.key(),
                                content_type='text/plain')
        else:
            return HttpResponseForbidden

    else:
        return HttpResponseNotAllowed('POST')
