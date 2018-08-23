import requests

class Auth():
    
    def generateToken(username='', password=''):
        with open('./soap/auth.xml', 'r') as myfile:
            data = myfile.read() 
            print(data % (username, password))
