import xml.etree.ElementTree as ET

from zadmin.soap.auth_request import AuthRequest
from zadmin.request import Request

class Auth():
    def __init__(self, webservice, username, password):
        self.webservice = webservice
        self.username = username
        self.password = password
        self.token = self.token()

    def token(self):
        try:
            xml = AuthRequest.authenticate % (self.username, self.password)
            r = Request.post(self.webservice, xml=xml.strip())
            return ET.fromstring(r.content).find('.//{urn:zimbraAdmin}authToken').text
        except Exception as e:
            print('err', e)