from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import logging
from watchdoge.authenticate import authenticate

logging.basicConfig(filename='debugLog.log')
logger = logging.getLogger(__name__)
check = '1337badwolf'

"""
In:
- username
- password
- check
Out fail:
- status
Out success:
- status
- loginData
"""
def auth(request):
    if request.method == "POST":
        if str(request.POST['username']) is None or str(request.POST['username']) is ''\
                or str(request.POST['password']) is None or str(request.POST['password']) is ''\
                or str(request.POST['check']) is None or str(request.POST['check']) is '':
            messages.add_message(request, messages.ERROR, "{'info':'Authentication error, empty field'}")
            logger.info('Auth failed, empty field.')
            return HttpResponse(request, status=400)
        # TODO get working
        elif str(request.POST['check']) is not check:
            messages.add_message(request, messages.ERROR, "{'info':'Authentication error, bad request'}")
            logger.info('Auth failed, bad request.')
            return HttpResponse(request, status=400)
        else:
            [authenticity, logindata] = authenticate(request)
            if authenticity is not 200:
                messages.add_message(request, messages.ERROR, "{'info':'Authentication error, faulty credentials'}")
                logger.info('Auth failed, faulty credentials.')
                return HttpResponse(request, status=authenticity)
            else:
                messages.add_message(request, messages.INFO, "{'info':'Authentication successful'}")
                logger.info('Auth successful.')
                return HttpResponse(request,
                                    status=authenticity,
                                    content_type='application/json',
                                    charset='utf-8',
                                    content=logindata)
    else:
        messages.add_message(request, messages.WARNING, "You can't do that.")
        logger.info('Auth failed, user did not make post request to api/auth/.')
        return HttpResponse(request, status=400)


def login(request):
    if request.method == 'POST':
        logger.info('Login post request.')
        return redirect('/api/auth/')
    else:
        return render(request, 'login.html')
        logger.info('Login page request.')