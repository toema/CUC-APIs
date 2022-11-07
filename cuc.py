from io import StringIO
import json
from pprint import pprint
from requests_toolbelt.utils import dump
from xmlrpc.client import Fault
from requests import Request,Session
from requests.auth import HTTPBasicAuth
import requests
import urllib3
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
class CUC:
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# headers = {'Content-type': 'content_type_value'}
    def __init__(self,username,password,cuc) -> None:
        self.username=username
        self.password=password
        self.cuc=cuc
    
    def Add_User(self,UserId,Extension,Template):
        headers = {'Accept':'application/json',"Connection": "keep-alive"}
        req={ "Alias": UserId,"DtmfAccessId": Extension}
        adminSession = Session()
        params = { 'templateAlias': 'voicemailusertemplate' }
        if Template=="":
            params = { 'templateAlias': 'voicemailusertemplate' }
        else:
            params = { 'templateAlias': Template }
        resp = requests.post( 
                f'https://{self.cuc}/vmrest/users',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                json = req,
                params=params,
                verify = False
                )    # tree=ElementTree.parse(response.content)
        
        data=resp
        try:
            return data
        except Fault as e:
            return e
    # data=responsejson
    def List_User(self,UserId,Extension):
        headers = {"Content-Type": "application/xml",'Accept':'application/json',"charset":"UTF-8","Connection": "keep-alive"}
        req={ "Alias": UserId,"DtmfAccessId": Extension}
        adminSession = requests.Session()
        params = { 'templateAlias': 'voicemailusertemplate' }
        resp = adminSession.get( 
                f'https://{self.cuc}/vmrest/users?templateAlias=voicemailusertemplate',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        data=resp.json()
        try:
            return data
        except Fault as e:
            return e
    def Get_User(self,UserId):
        headers = {"Content-Type": "application/xml",'Accept':'application/json',"charset":"UTF-8","Connection": "keep-alive"}
        # req={ "Alias": UserId,"DtmfAccessId": Extension}
        adminSession = requests.Session()
        # params = { 'templateAlias': 'voicemailusertemplate' }
        resp = adminSession.get( 
                f'https://{self.cuc}/vmrest/users?query=(alias%20is%20{UserId})',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        data=resp.json()
        try:
            return data
        except Fault as e:
            return e
    def Delete_User(self,UserId):
        headers = {"Content-Type": "application/xml",'Accept':'application/json',"charset":"UTF-8","Connection": "keep-alive"}
        # req={ "Alias": UserId,"DtmfAccessId": Extension}
        adminSession = requests.Session()
        res = adminSession.get( 
                f'https://{self.cuc}/vmrest/users?query=(alias%20is%20{UserId})',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        dat=res.json()
        try:
            objectid=dat["User"]["ObjectId"]
        except:
            return dat

        
        # params = { 'templateAlias': 'voicemailusertemplate' }
        DeleteAction = adminSession.delete( 
                f'https://{self.cuc}/vmrest/users/{objectid}',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        data=DeleteAction
        try:
            return data
        except Fault as e:
            return e
    def Get_Templates(self):
        headers = {'Accept':'application/json',"charset":"UTF-8","Connection": "keep-alive"}
        
        adminSession = requests.Session()
        params = { 'templateAlias': 'voicemailusertemplate' }
        resp = adminSession.get( 
                f'https://{self.cuc}/vmrest/usertemplates',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        data=resp.json()
       
        try:
            return data
        except Fault as e:
            return e
    def Get_User_Extensions(self,UserId):
        headers = {"Content-Type": "application/xml",'Accept':'application/json',"charset":"UTF-8","Connection": "keep-alive"}
        # req={ "Alias": UserId,"DtmfAccessId": Extension}
        adminSession = requests.Session()
        res = adminSession.get( 
                f'https://{self.cuc}/vmrest/users?query=(alias%20is%20{UserId})',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        dat=res.json()
        objectid=dat["User"]["ObjectId"]
        # print(objectid)

        
        GetUserExts = adminSession.get( 
                f'https://{self.cuc}/vmrest/users/{objectid}/alternateextensions',
                auth=HTTPBasicAuth( f"{self.username}", f"{self.password}" ),
                headers=headers,
                verify = False
                )
        data=GetUserExts.json()
        try:
            return data
        except Fault as e:
            return e
        # for Alias in data["User"]:
        #     print(Alias["Alias"])