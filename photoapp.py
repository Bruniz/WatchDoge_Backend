import logging
import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from watchdogesite.models import Photo

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
            self.response.out.write(response_data)
        else:
            response_data = {'result': 'OK', 'url': 'NA'}
            self.response.out.write(response_data)

    def get(self):
        self.error(405)

# Method for uploading a photo
# Get url for upload from calling above method first
# params: 'reportID' and the file
# returns JSON
# Success: {'result': "OK"}
# Fail: error 500
class PhotoUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    logger.info('photoupload')
    def post(self):
        logger.info('post')
        try:
            logger.info('try')
            upload = self.get_uploads()[0]
            logger.info('upload')
            photo = Photo(
                reportID=self.request.get('Reportid'),
                blob_key=upload.key())
            logger.info('photo')
            photo.put()
            logger.info(self.request.get('Reportid'))
            logger.info(str(self.request))
            self.response.out.write(200)

        except:
            logger.error('server error, except', 500)
            self.error(500)

app = webapp2.WSGIApplication([
    ('/get_upload_url', PhotoUploadUrlCreator),
    ('/upload_photo', PhotoUploadHandler),
], debug=True)