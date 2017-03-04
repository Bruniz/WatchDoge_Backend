import logging
import re
import webapp2
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from watchdogesite.models import Photo, Report

AUTH = "AMmfu6Zc_3BPr4ehPamOOQP"
logger = logging.getLogger(__name__)

# Method for fetching a photo upload url
# Should make a POST to "/upload_url" and params should be:
# params: 'AUTH': "AMmfu6Zc_3BPr4ehPamOOQP"
# returns JSON
# Success: {'result': "OK", 'url': "long url to send photo to"}
# Fail: {'result': "ERROR", 'url': "NA"}
class PhotoUploadUrlCreator(webapp2.RequestHandler):
    def post(self):
        logger.info(" url post create")
        if self.request.get('AUTH') == AUTH:
            upload_url = blobstore.create_upload_url('/upload_photo')
            response_data = {upload_url}
            logger.info('')
            self.response.out.write(response_data)
        else:
            self.error(500)

    def get(self):
        self.error(405)

class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    logger.info('photoupload')
    def post(self):
        r = str(self.request)
        try:
            x = re.search('<REPORTID>(.+?)<REPORTID>', r)
            if x:
                reportID = x.group(1)
                logger.info(reportID)
                upload = self.get_uploads()[0]
                logger.info('upload object')
                photo = Photo(
                    reportID=reportID,
                    serving_url = images.get_serving_url(upload.key()))
                photo.put()
                logger.info('photo saved')

                self.response.out.write(200)
            else:
                self.error(500)
        except:
            logger.error('server error, except', 500)
            self.error(500)

app = webapp2.WSGIApplication([
    ('/get_upload_url', PhotoUploadUrlCreator),
    ('/upload_photo', PhotoUploadHandler),
], debug=True)