import xml.etree.ElementTree as ET

from zadmin.soap.account import AccountRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Account():
    
    def __init__(self, auth=''):
        self.auth = auth

    def get_all_accounts(self, hostname):
        try:
            xml = AccountRequest.get_all_accounts_request % (self.auth.token, self.auth.username, hostname)
            r = Request.post(self.auth.webservice, xml=xml.strip()) 
        
            if r.status_code == 200:
                e = ET.fromstring(r.content).findall('.//{urn:zimbraAdmin}account')        

                acc = []
                for x in e:
                    cos = None
                    for i in x.getchildren():
                        if i.attrib['n'] == 'zimbraCOSId':
                            cos = i.text
                    
                    acc.append({'name':x.attrib['name'], 'id':x.attrib['id'], 'cos': cos})
                
                return {'success' : True, 'response' : {
                    'accounts' : acc
                }}            
            

            e = ET.fromstring(r.content).find('.//{urn:zimbra}Code').text
            return {'success' : False, 'response' : {
                'code' : e
            }}

        except Exception as e:
            return {'success' : False, 'response' : {
                'code' : e.message
            }}

    def get(self, account):

        try:
            xml = AccountRequest.get_account_request % (self.auth.token, self.auth.username, account)
            r = Request.post(self.auth.webservice, xml=xml.strip())
            
            if r.status_code == 200:
                e = ET.fromstring(r.content).find('.//{urn:zimbraAdmin}account')
                a = ET.fromstring(r.content).findall('.//{urn:zimbraAdmin}')
               
                print(r.content)
                
                #'zimbraPrefMailSignature' : e.attrib['zimbraPrefMailSignature']
                return {'success' : True, 'response' : {
                    'account' : e.attrib['name'],
                    'id' : e.attrib['id'],
                    'attr' : {
                        
                    }
                }}
            
            e = ET.fromstring(r.content).find('.//{urn:zimbra}Code').text
            return {'success' : False, 'response' : {
                'code' : e
            }}

        except Exception as e:
            return {'success' : False, 'response' : {
                'code' : e.message
            }}

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

    def update(self, account, password=None, zimbraCosId=None):

        try:
            xml = AccountRequest.update_account_request % (self.auth.token, self.auth.username, account, password, zimbraCosId)
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
