import xml.etree.ElementTree as ET

from zadmin.soap.backup import BackupQueryRequest
from zadmin.request import Request
from zadmin.auth import Auth

class BackupQuery():
    
    def __init__(self, auth=''):
        self.auth = auth

    def get(self, account='all'):
        try:
            xml = BackupQueryRequest.backup_account_query_request % (self.auth.token, self.auth.username, account)
            r = Request.post(self.auth.webservice, xml=xml.strip())
            
            if r.status_code == 200:
                e = ET.fromstring(r.content).findall('.//{urn:zimbraAdmin}backup')
                l_bkp = [ {'label':x.attrib['label'] } for x in e]

                return {'success' : True, 'response' : {
                    'backup' : l_bkp
                }}
            
            e = ET.fromstring(r.content).find('.//{urn:zimbra}Code').text
            return {'success' : False, 'response' : {
                'code' : e
            }}

        except Exception as e:
            return {'success' : False, 'response' : {
                'code' : e.message
            }}
