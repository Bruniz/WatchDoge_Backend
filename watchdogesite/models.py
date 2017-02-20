from django.db import models
from google.appengine.ext import db
import webapp2
import datetime


# Create your models here.
class Report(db.Model):
    type = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    pets = db.StringProperty(required=True)
    entry = db.StringProperty(required=True)
    date = db.DateProperty()

    meta = {
        'indexes': [
            'type',
            'title'
        ]
    }
