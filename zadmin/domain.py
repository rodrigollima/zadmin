import xml.etree.ElementTree as ET

from zadmin.soap.domain import DomainRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Domain():
    
    def __init__(self, auth=''):
        self.auth = auth

    '''
    
    '''
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

    def count_accounts_by_class_of_service(self, hostname):
            """
            Count all accounts by Zimbra Class of Service
            """
            try:
                xml = DomainRequest.count_accounts_by_class_of_service % (self.auth.token, self.auth.username, hostname)
                print(xml)
                r = Request.post(self.auth.webservice, xml=xml.strip())

                if r.status_code == 200:
                    
                    print(r.content)
                    
                    e = ET.fromstring(r.content).findall('.//{urn:zimbraAdmin}cos')
                    l_cos = [ {'label':x.attrib['name'], 'id':x.attrib['id'], 'quantity':x.text} for x in e]

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
