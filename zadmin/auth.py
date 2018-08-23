import requests
import xml.etree.ElementTree as ET

from zadmin.soap.auth_request import AuthRequest
from zadmin.request import Request

class Auth():
    
    def generateToken(webservice='', username='', password=''):
        try:
            xml = AuthRequest.authenticate % (username, password)
            r = Request.post(webservice, xml=xml)

            return ET.fromstring(r.content).find('.//{urn:zimbraAdmin}authToken').text
        except Exception as e:
            print(e)