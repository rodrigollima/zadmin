# zadmin
A simple Python library to provide access to a complex Zimbra Soap interface.

## Installation
`pip install git+https://github.com/rodrigollima/zadmin.git`

### Basics
For all request you need an Auth token instance
```python
   from zadmin.auth import Auth
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   auth.token
```

### Domain creation
```python
   from zadmin.auth import Auth
   from zadmin.domain import Domain
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   domain = Domain(auth)
   d = domain.create(hostname='newhost.tld')
```

### Accoun creation
```python
   from zadmin.auth import Auth
   from zadmin.account import Account
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   account = Account(auth)
   a = account.create(account='testeprov@inova.net', password='fdas@#F555AFSD',zimbraCosId='8e97e282-8aa0-4ac4-96fb-7e2e7620c0a4')
```

### List COS
```python
   from zadmin.auth import Auth
   from zadmin.cos import Cos
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   cos = Cos(auth)
   c = cos.list()
```

### Feature List
* `Domain`
  * creation
* `Account`
  * creation
* `COS`
  * list

