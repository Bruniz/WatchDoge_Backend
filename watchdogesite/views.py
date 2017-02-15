from django.shortcuts import render
from django.shortcuts import redirect
from google.appengine.ext import db
from watchdogesite.models import Review

import datetime
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def reviews(request):
    reviews = db.GqlQuery("SELECT * FROM Review")
    logger.info(reviews)
    return render(request, "reviews.html", {'reviews': reviews})


def add_review(request):
    if request.method == 'POST':
        items = request.POST
        r = Review(location=items['location'], description=items['review'], title=items['title'],
                   star_rating=int(items['stars']))
        r.date = datetime.datetime.now().date()
        r.put()
        return redirect('/reviews')
    else:
        return render(request, 'add_review.html')
