from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseServerError
from django.http import HttpResponseForbidden
from google.appengine.ext.db import TransactionFailedError
from watchdogesite.models import Report
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging
import hashlib

logger = logging.getLogger(__name__)

p = '1337badwolf'
m = hashlib.sha1()
m.update(p)
CHECK = m.hexdigest()


@csrf_exempt
def add(request):

    # Add new report
    if request.method == 'POST':
        try:
            items = request.POST
            if ('check' in items and 'type' in items and
                    'desc' in items and 'title' in items and
                    'pets' in items and 'entry' in items):
                if request.POST['check'] is not CHECK:
                    return HttpResponseForbidden
                try:
                    r = Report(type=items['type'], description=items['desc'], title=items['title'],
                               pets=items['pets'], entry=items['entry'])
                    r.date = datetime.datetime.now().date()
                    r.put()
                    return HttpResponse(r.key(),
                                        content_type='text/plain')
                except TransactionFailedError, e:
                    logger.error('Failed to save report')
                    logger.error(e)
                    return HttpResponseServerError('Failed to receive report')
            else:
                return HttpResponseForbidden
        except Exception, er:
            logger.error('Method fail')
            logger.error(er)
            return HttpResponseServerError('API fail')

    else:
        return HttpResponseNotAllowed('POST')
