import requests

class Request:

    def post(url = '', xml=''):
        headers = { 'Content-Type': 'application/soap+xml' }
        
        return requests.post(webservice, data=xml, headers=headers, verify=False)