import xml.etree.ElementTree as ET

from zadmin.soap.domain import DomainRequest
from zadmin.request import Request
from zadmin.auth import Auth

class Domain():
    
    def __init__(self, auth=''):
        self.auth = auth

    '''
    from zadmin.auth import Auth
    from zadmin.domain import Domain
    a = Auth('https://disaster01.a.inova.com.br:7071/service/admin/soap', 'admin', '1sta+his1')
    d = Domain(a)
    d.create(hostname='mailability.mx')
    '''
    def create(self, hostname=''):
        try:
            print(self.auth.token)
            xml = DomainRequest.create_domain_request % (self.auth.token, self.auth.username, hostname)
            print(xml.strip())
            r = Request.post(self.auth.webservice, xml=xml.strip())
            print(r)
            if r.status_code == 200:
                return {'success' : True, 'response' : r.text}
            
            return {'success' : False, 'response' : r.content}
        except Exception as e:
            print(e)

