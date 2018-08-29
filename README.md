# zadmin
A simple Python library to provide access to a complex Zimbra Soap interface.

## Installation
`pip install git+https://github.com/rodrigollima/zadmin.git`

## Basics
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

## Feature List
* `Domain`
  * creation

