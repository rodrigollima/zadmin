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

            if r.status_code == 200:
                e = ET.fromstring(r.content).find('.//{urn:zimbraAdmin}domain')

                return {'success' : True, 'response' : {
                    'domain' : e.attrib['name'],
                    'id' : e.attrib['id']
                }}
            
            e = ET.fromstring(r.content).find('.//{urn:zimbra}Code').text
            return {'success' : False, 'response' : {
                'code' : e
            }}

        except Exception as e:
            return {'success' : False, 'response' : {
                'code' : e.message
            }}

