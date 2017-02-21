import requests
import logging
import json

logging.basicConfig(filename='debugLog.log', level=logging.DEBUG)


def authenticate(request):
    s = requests.session()
    url = "https://asukassivusto.tys.fi/kirjautuminen/"
    get_request = s.get(url)

    username = request.GET.get("username")
    password = request.GET.get("password")

    if True is True:
        logging.debug('Authenticating:\n' +
                      ' username: ' + username +
                      '\n password: ' + password)

    # Login
    param = {
        '__VIEWSTATE': '/wEPDwUJNDMxNzM2NjU5D2QWAgICD2QWBgIBD2QWAmYPZBYGAgEPDxYCHgRUZXh0BTo8YSBocmVmPSIvb21hdHRpZWRv' +
                       'dC8iPlBhdHJpayBNYXJjdXMgU2ViYXN0aWFuIEhpbGxuZXI8L2E+ZGQCBQ8PFgIeB1Zpc2libGVoZGQCCQ8PFgIeC1Bv' +
                       'c3RCYWNrVXJsBQ8va2lyamF1dHVtaW5lbi9kZAIDD2QWAgICD2QWAgIBDw8WAh8ABR9QYXRyaWsgTWFyY3VzIFNlYmFz' +
                       'dGlhbiBIaWxsbmVyZGQCBQ9kFgICAg8WAh8BZxYEAgEPFgIeC18hSXRlbUNvdW50AgQWCGYPZBYEZg8VBAAGQWN0aXZl' +
                       'AAdFdHVzaXZ1ZAIBDxYEHwNmHwFoZAIBD2QWBGYPFQQQL2hha2VtdXN0YXJqb3VzLwAAEUhha2VtdXMgLyBUYXJqb3Vz' +
                       'ZAIBDxYCHwMCAhYEAgEPZBYCZg8VBBgvaGFrZW11c3RhcmpvdXMvaGFrZW11cy8AAAdIYWtlbXVzZAICD2QWAmYPFQQY' +
                       'L2hha2VtdXN0YXJqb3VzL3RhcmpvdXMvAAAHVGFyam91c2QCAg9kFgRmDxUEDy92dW9rcmFzb3BpbXVzLwAADVZ1b2ty' +
                       'YXNvcGltdXNkAgEPFgIfAwICFgQCAQ9kFgJmDxUENC92dW9rcmFzb3BpbXVzL2FzdW1pc2Vua2Vza2V5dHlzamF2YWxp' +
                       'dnVva3Jhc29waW11cy8AACdBc3VtaXNlbmtlc2tleXR5cyBqYSB2w6RsaXZ1b2tyYXNvcGltdXNkAgIPZBYCZg8VBB0v' +
                       'dnVva3Jhc29waW11cy90YWxvbmtpcmphb3RlLwAADVRhbG9ua2lyamFvdGVkAgMPZBYEZg8VBA0vbWFrc3V0aWVkb3Qv' +
                       'AAALTWFrc3V0aWVkb3RkAgEPFgIfAwIBFgICAQ9kFgJmDxUEHi9tYWtzdXRpZWRvdC92YWt1dWRlbnBhbGF1dHVzLwAA' +
                       'EVZha3V1ZGVuIHBhbGF1dHVzZAIDDxYCHwMCBBYIZg9kFgRmDxUEDS9hc3VudG9rb2hkZS8AAAtBc3VudG9rb2hkZWQC' +
                       'AQ8WAh8DAgIWBAIBD2QWAmYPFQQeL2FzdW50b2tvaGRlL2FzdWthc3RvaW1pa3VudGEvAAAQQXN1a2FzdG9pbWlrdW50' +
                       'YWQCAg9kFgJmDxUEJS9hc3VudG9rb2hkZS9hc3VudG9rb2h0ZWVudGllZG90dGVldC8AABhBc3VudG9rb2h0ZWVuIHRp' +
                       'ZWRvdHRlZXRkAgEPZBYEZg8VBBEvSHVvbmVpc3Rva29ydHRpLwAAD0h1b25laXN0b2tvcnR0aWQCAQ8WBB8DZh8BaGQC' +
                       'Ag9kFgRmDxUEEi9hc3VtaXNlbnBhbHZlbHV0LwAAEUFzdW1pc2VuIHBhbHZlbHV0ZAIBDxYCHwMCBxYOAgEPZBYCZg8V' +
                       'BB8vYXN1bWlzZW5wYWx2ZWx1dC92aWthaWxtb2l0dXMvAAAMVmlrYWlsbW9pdHVzZAICD2QWAmYPFQQdL2FzdW1pc2Vu' +
                       'cGFsdmVsdXQvdHlzYm9va2luZy8AAApUWVNCb29raW5nZAIDD2QWAmYPFQQiL2FzdW1pc2VucGFsdmVsdXQvdmVkZW5r' +
                       'dWx1dHVrc2V0LwAAEFZlZGVuIGt1bHV0dWtzZXRkAgQPZBYCZg8VBB0vYXN1bWlzZW5wYWx2ZWx1dC9reWxhdmVya2tv' +
                       'LwAAC0t5bMOkdmVya2tvZAIFD2QWAmYPFQQfL2FzdW1pc2VucGFsdmVsdXQvYXZhaW5saXN0YXVzLwAADEF2YWlubGlz' +
                       'dGF1c2QCBg9kFgJmDxUEIC9hc3VtaXNlbnBhbHZlbHV0L2F2YWlubHVvdnV0dXMvAAANQXZhaW5sdW92dXR1c2QCBw9k' +
                       'FgJmDxUEIS9hc3VtaXNlbnBhbHZlbHV0L2hhaXJpb2lsbW9pdHVzLwAAEEjDpGlyacO2aWxtb2l0dXNkAgMPZBYEZg8V' +
                       'BA8vaXJ0aXNhbm9taW5lbi8AAA1JcnRpc2Fub21pbmVuZAIBDxYEHwNmHwFoZGS5VrRQNnaTjNg9xixcq22NHs9xMGgY' +
                       '5j2tQ/vteGoT6Q==',
        '__EVENTVALIDATION': '/wEdAAduD/E9TYg+aa06j8UpzMO7Gf+wSOndHsCQ+o9sT/0mU245E5uubRcXaETxy0g7mtIMyErqzqYZ3lzvTf' +
                       'sRxSHbZbxrSGUoBpmDTC9r3iV9K5BF8lFVwQTZiqX8cLisZ7ThESDm/OoUu8Vx/PJxtByikXvT1MRrqJORXjGSeLyW0q' +
                       'MYkRJllU3QY4AZA/wLEcw=',
        'Kirjautuminen_TAAAAAAAA$userName': username,
        'Kirjautuminen_TAAAAAAAA$passWord': password,
        'Kirjautuminen_TAAAAAAAA$btnLogin': 'Kirjaudu',
    }
    post_request = s.post(url, data=param)

    # Check for successful login
    try:
        redir = post_request.history.pop()
    except IndexError:
        logging.debug('Auth failed, wrong credentials')
        return [401, 'Wrong credentials']
    if redir.status_code == 302:
        logging.debug('Successful login!\n' +
                      'Content: ' + str(post_request.read()))
    else:
        logging.debug('Something unexpected happened! Redirect status code: ' + str(redir.status_code) + '\n' +
                      'Content: ' + str(redir.read()))
        return [501, 'Unexpected status']

    # Get data from cookie
    usertoken_json = json.load(redir.cookies.get('usertoken'))
    ValittuKohde_json = json.load(redir.cookies.get('ValittuKohde'))

    # Return authentication status and data from cookie
    data = json.load('{' + usertoken_json + ',' + ValittuKohde_json + '}')
    return [200, data]
