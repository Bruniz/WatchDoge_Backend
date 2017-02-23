import datetime
import logging

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from google.appengine.ext import db
from google.appengine.ext.blobstore import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import json
from django.http import HttpResponse

from watchdogesite.models import *

logger = logging.getLogger(__name__)

AUTH = "AMmfu6Zc_3BPr4ehPamOOQP"

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def reports(request):
    reports = db.GqlQuery("SELECT * FROM Report")
    logger.info(reports)
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

# Method for fetching a photo upload url
# Should make a POST to "/upload_url" and params should be:
# params: 'AUTH': "AMmfu6Zc_3BPr4ehPamOOQP"
# returns JSON
# Success: {'result': "OK", 'url': "long url to send photo to"}
# Fail: {'result': "ERROR", 'url': "NA"}
@csrf_exempt
def get_upload_url(request):
    if request.method == 'POST':
        if request.POST['AUTH'] == AUTH:
            upload_url = blobstore.create_upload_url('/upload_photo')
            response_data = {'result': 'OK', 'url': upload_url}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            response_data = {'result': 'ERROR', 'url': "NA"}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return redirect('/')

# Method handling upload of photos
# Should make a POST to the URL provided by the get_upload_url method
# params: 'file': "theimage.png, 'reportID': "ID of report the photo belongs to"
# returns JSON
# Success: {'result': "OK"}
# Fail: {'result': "ERROR 500"}
@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        handler = blobstore_handlers.BlobstoreUploadHandler
        try:
            upload = handler.get_uploads()[0]
            photo = Photo(
                reportID="report1",
                blob_key=upload.key())
            photo.put()

            response_data = {'result': 'OK'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        except:
            response_data = {'result': 'ERROR 500'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        return redirect('/')

