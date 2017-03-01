import sys
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

p = "1337badwolf"
m = hashlib.sha1()
m.update(p)
CHECK = m.hexdigest()


@csrf_exempt
def add(request):
    logger.info('Report recieved')
    # Add new report
    if request.method == 'POST':
        logger.info('Report was POST')
        try:
            items = request.POST
            logger.info(items)
            if ('type' in items and
                    'desc' in items and 'title' in items and
                    'pets' in items and 'entry' in items):
                logger.info('all params in post')
                # if request.POST['check'] is not p:
                #     logger.error(request.POST['check'])
                #     logger.error('Wrong check')
                #     return HttpResponseForbidden
                try:
                    logger.info('Try')
                    r = Report(type=items['type'], description=items['desc'], title=items['title'],
                               pets=items['pets'], entry=items['entry'])
                    logger.info(datetime.datetime.now().date())
                    r.date = datetime.datetime.now().date()
                    logger.info(r)
                    logger.info(datetime.datetime.now().date())
                    r.put()
                    r.save()
                    logger.info(r.key())
                    return HttpResponse(r.key(),
                                        content_type='text/plain')
                except TransactionFailedError, e:
                    logger.error('Failed to save report')
                    logger.error(e)
                    return HttpResponseServerError('Failed to receive report')
            else:
                logger.error('Mega if fail')
                return HttpResponseForbidden
        except Exception:
            logger.error('Method fail')
            logger.error(sys.exc_info()[0])
            return HttpResponseServerError('API fail')

    else:
        return HttpResponseNotAllowed('POST')
