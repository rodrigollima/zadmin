import xml.etree.ElementTree as ET

from zadmin.soap.account import AccountRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Account():
    
    def __init__(self, auth=''):
        self.auth = auth

    def create(self, account, password='pwdPWD@@PWDpwd', zimbraCosId=''):

        try:
            xml = AccountRequest.create_account_request % (self.auth.token, self.auth.username, account, password, zimbraCosId)
            r = Request.post(self.auth.webservice, xml=xml.strip())
            
            if r.status_code == 200:
                e = ET.fromstring(r.content).find('.//{urn:zimbraAdmin}account')

                return {'success' : True, 'response' : {
                    'account' : e.attrib['name'],
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

    def rename(self, id, account):

        try:
            xml = AccountRequest.rename_account_request % (self.auth.token, self.auth.username, id, account)
            r = Request.post(self.auth.webservice, xml=xml.strip())
            
            if r.status_code == 200:
                e = ET.fromstring(r.content).find('.//{urn:zimbraAdmin}account')

                return {'success' : True, 'response' : {
                    'account' : e.attrib['name'],
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