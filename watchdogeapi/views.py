from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
import json
from watchdogesite.models import Report
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def add(self, request):

    # Add new report
    if request.method == 'POST':
        items = request.POST
        r = Report(type=items['type'], description=items['desc'], title=items['title'],
                   pets=items['pets'], entry=items['entry'])
        r.date = datetime.datetime.now().date()
        r.put()
        data = {'id': r.id}
        return HttpResponse(json.dumps(data),
                            status=200,
                            content_type='application/json')

    else:
        return HttpResponseNotAllowed('POST')
