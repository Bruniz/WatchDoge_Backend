from django.db import models
from google.appengine.ext.blobstore import blobstore
from google.appengine.ext import db
from google.appengine.ext import ndb
import webapp2
import datetime


# Create your models here.
class Report(ndb.Model):
    type = ndb.StringProperty(required=True)
    title = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    pets = ndb.StringProperty(required=True)
    entry = ndb.StringProperty(required=True)
    date = ndb.DateProperty(auto_now_add=True)

    meta = {
        'indexes': [
            'type',
            'title'
        ]
    }
    @classmethod
    def all_reports_by_date(cls):
        return cls.query().order(-cls.date)


class Photo(ndb.Model):
    reportID = ndb.StringProperty()
    serving_url = ndb.StringProperty(indexed=False)
