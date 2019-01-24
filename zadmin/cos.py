import xml.etree.ElementTree as ET
#import xmltodict 

from zadmin.soap.cos import CosRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Cos():
    
    def __init__(self, auth=''):
        self.auth = auth

    def list(self):
        try:
            xml = CosRequest.list_cos_request % (self.auth.token, self.auth.username)
            r = Request.post(self.auth.webservice, xml=xml.strip())

            if r.status_code == 200:
                e = ET.fromstring(r.content).findall('.//{urn:zimbraAdmin}cos')
                l_cos = [ {'label':x.attrib['name'], 'id':x.attrib['id']} for x in e]

                return {'success' : True, 'response' : {
                    'cos' : l_cos
                }}
            
            e = ET.fromstring(r.content).find('.//{urn:zimbra}Code').text
            return {'success' : False, 'response' : {
                'code' : e
            }}

        except Exception as e:
            return {'success' : False, 'response' : {
                'code' : e.message
            }}

    '''