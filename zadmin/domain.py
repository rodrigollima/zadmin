import xml.etree.ElementTree as ET
import xmltodict 

from zadmin.soap.domain import DomainRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Domain():
    
    def __init__(self, auth=''):
        self.auth = auth

    def create(self, hostname=''):
        try:
            xml = DomainRequest.create_domain_request % (self.auth.token, self.auth.username, hostname)
            
            r = Request.post(self.auth.webservice, xml=xml.strip())
            response = xmltodict.parse(r.text)

            if r.status_code == 200:
                return {'success' : True, 'response' : response}
            
            return {'success' : False, 'response' : response}
        except Exception as e:
            print(e)

