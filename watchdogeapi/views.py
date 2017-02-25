from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
import json
from watchdogesite.models import Report
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def add(request):

    # Add new report
    if request.method == 'POST':
        items = request.POST
        r = Report(type=items['type'], description=items['desc'], title=items['title'],
                   pets=items['pets'], entry=items['entry'])
        r.date = datetime.datetime.now().date()
        r.put()
        return HttpResponse(r.key(),
                            content_type='text/plain')

    else:
        return HttpResponseNotAllowed('POST')
