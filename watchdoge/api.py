from django.contrib import messages
from django.http import HttpResponse
import logging
from watchdoge.authenticate import authenticate

logging.basicConfig(filename='debugLog.log', level=logging.DEBUG)
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
            messages.add_message(request, messages.ERROR, "{'info':'Authentication error'}")
            logging.DEBUG('Auth failed, empty field.')
            return HttpResponse(request, status=400)
        elif str(request.POST['check']) is not check:
            messages.add_message(request, messages.ERROR, "{'info':'Authentication error'}")
            logging.DEBUG('Auth failed, bad request.')
            return HttpResponse(request, status=400)
        else:
            [authenticity, logindata] = authenticate(request)
            if authenticity is not 200:
                messages.add_message(request, messages.ERROR, "{'info':'Authentication error'}")
                return HttpResponse(request, status=authenticity)
            else:
                messages.add_message(request, messages.INFO, "{'info':'Authentication successful'}")
                return HttpResponse(request,
                                    status=authenticity,
                                    content_type='application/json',
                                    charset='utf-8',
                                    content=logindata)
    else:
        messages.add_message(request, messages.WARNING, "You can't do that.")
        return HttpResponse(request, status=400)