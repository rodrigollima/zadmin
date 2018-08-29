import requests

class Request:

    def post(url = '', xml=''):
        headers = { 'Content-Type': 'application/soap+xml' }
        
        return requests.post(url, data=xml, headers=headers, verify=False)