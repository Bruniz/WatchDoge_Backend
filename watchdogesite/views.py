import datetime
import logging
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from google.appengine.ext import db
from watchdogesite.models import Report
from watchdogesite.models import Photo

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def reports(request):
    reports = db.GqlQuery("SELECT * FROM Report")

    return render(request, "reports.html", {'reports': reports})

@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        items = request.POST
        r = Report(type=items['type'], description=items['desc'], title=items['title'],
                   pets=items['pets'], entry=items['entry'])
        r.date = datetime.datetime.now().date()
        r.put()
        return redirect('/reports')
    else:
        return render(request, 'add_report.html')
