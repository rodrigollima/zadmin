import xml.etree.ElementTree as ET

from zadmin.soap.server import ServerRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Server():
    """
    A class used to mostly usefull admin commands for Zimbra
    """
    def __init__(self, auth=''):
        self.auth = auth


    def count_accounts_by_class_of_service(self, domain=''):
        """
        Count all accounts by Zimbra Class of Service
        """
        try:
            xml = ServerRequest.count_accounts_by_class_of_service % (self.auth.token, self.auth.username)
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

        