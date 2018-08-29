import xml.etree.ElementTree as ET

from zadmin.soap.domain import DomainRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Domain():
    
    def __init__(self, auth=''):
        self.auth = auth

    def create(self, hostname=''):
        try:
            print(self.auth.token)
            xml = DomainRequest.create_domain_request % (self.auth.token, self.auth.username, hostname)
            
            r = Request.post(self.auth.webservice, xml=xml.strip())
            if r.status_code == 200:
                return {'success' : True, 'response' : r.text}
            
            return {'success' : False, 'response' : r.content}
        except Exception as e:
            print(e)

