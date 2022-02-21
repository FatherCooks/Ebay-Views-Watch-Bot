import re
import sys
import requests
import time
import random
import requests
import json
from time import sleep
import datetime
from colorama import init
import threading
from bs4 import BeautifulSoup
from threading import Semaphore
from colorama import Fore, Back, Style
import logging
import importlib.util
sys.path.append("Utilities")
#import settings
import credentials
import get_proxy
import data
from requests import exceptions as requestsExceptions
from Utilities.Captcha import FB_captcha


init(autoreset=True)

class Watch:
    def __init__(self, EBAY:object, email, password, i ):
        self.lock = EBAY.lock
        self.sem = EBAY.sem
        self.URL = EBAY.URL
        self.email = email
        self.password = password
        self.task = i
        self.s = requests.Session()
        
    
        self.start()
        

        
    def start(self):
        self.chooseProxy()
        self.task
        self.getSession()
        self.login()
        time.sleep(30)
        self.watchDetails()
        
        self.sem.release()
        return

    def chooseProxy(self):
        self.s.proxies.update(get_proxy.get_proxies())
        return
    
    def getSession(self):
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , "Getting Session")
        self.lock.release()
        
        while True:
            try:
                
                request = self.s.get(data.signIn_session, headers=data.Headers.signIn)
                
                soup = BeautifulSoup(request.text, 'html.parser')
                self.rqid = soup.find('input', {'name': 'rqid'}).get('value')
                self.guid = soup.find('input', {'name': 'lkdhjebhsjdhejdshdjchquwekguid'}).get('value')
                self.srt2 = soup.find('input', {'name': 'srt'}).get('value')
                print(self.srt2)
                
                token = str(re.findall(r'("csrfAjaxToken".*csrfSclConnectToken")',request.text)).strip()[2:-24]
                id = str(re.findall(r'\[(.*?)\]', request.text)[111]).strip()[19:-632]

                csrf = json.loads('{'+token+'}')
                mid = json.loads('{'+id+'}')
                #print(csrf, mid)
                self.csrfToken = csrf["csrfAjaxToken"]
                self.dfpmid = mid["dfpmid"]
                #p = soup.find('div', {'id': 'srt'}).get('value')
                print(self.s.cookies)
                
                
                 
                return
            
            except requests.exceptions.ConnectionError as connectionerror:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[CONNECTION ERROR]", Fore.RED+str(connectionerror))
                self.lock.release()
                continue
            except requests.exceptions.Timeout as timeout:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[TIMEOUT ERROR]", Fore.RED+str(timeout))
                self.lock.release()
                continue
            except requests.exceptions.RequestException as err:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[ERROR]", Fore.RED+str(err))
                self.lock.release()
                continue
            except requests.exceptions.ProxyError as proxErr:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[PROXY ERROR]", Fore.RED+str(proxErr))
                self.lock.release()
                self.chooseProxy()
                continue
        

    def watchDetails(self):
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , "Getting Watch Details")
        self.lock.release()
        
        while True:
            try:
                
                #if self.logged_in == True:
                    
                request = self.s.get(self.URL, headers=data.Headers.addViews)              

                u = str(re.findall(r'("addAjaxCSRF".*)remo',request.text)).strip()[2:-4]
                print(u)

                '''while u == "[]":
                    
                    print("Retrying Login")
                    self.login()
                else:
                    pass'''
                self.json_token = json.loads('{'+u+'}')
                
                return
            
            except requests.exceptions.ConnectionError as connectionerror:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[CONNECTION ERROR]", Fore.RED+str(connectionerror))
                self.lock.release()
                continue
            except requests.exceptions.Timeout as timeout:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[TIMEOUT ERROR]", Fore.RED+str(timeout))
                self.lock.release()
                continue
            except requests.exceptions.RequestException as err:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[ERROR]", Fore.RED+str(err))
                self.lock.release()
                continue
            except requests.exceptions.ProxyError as proxErr:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[PROXY ERROR]", Fore.RED+str(proxErr))
                self.lock.release()
                self.chooseProxy()
                continue
                
                
    def login(self):
        
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"Logging in {self.email}")
        self.lock.release()
        
        while True:
            try:
                
                self.logged_in = False
        
                payload = {
                    'userid': "ludlamhalsy27@gmail.com",#self.email,
                    'pass': "41Lavish__",#self.password,
                    'kmsi-unchecked': '1',
                    'kmsi': '1',
                    'i1': '',
                    'pageType': '-1',
                    'returnUrl': 'https://www.ebay.com/',
                    'srt': self.csrfToken,
                    'fypReset': '',
                    'ICurl': '',
                    'src': '',
                    'AppName': '',
                    'srcAppId': '',
                    'errmsg': '',
                    'rtmData': 'PS=T.0',
                    'rqid': self.rqid,
                    'lkdhjebhsjdhejdshdjchquwekguid': self.guid,
                    'recgUser': '',
                    'hbi': '0',
                    'lastAttemptMethod': 'password',
                    'showWebAuthnOptIn': '1',
                    'mid': self.dfpmid,   #PARAM MAY CHANGE IN THE NEAR FUTURE
                    'isRecgUser': 'false'
                    }
                
                
                request = self.s.post(data.signIn_URL,headers=data.Headers.login, timeout=12, allow_redirects=False)
                print(request.url, request.text)
                if 'SUCCESS' in request.text:
                    self.logged_in == True
                
                return
            
            except requests.exceptions.ConnectionError as connectionerror:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[CONNECTION ERROR]", Fore.RED+str(connectionerror))
                self.lock.release()
                continue
            except requests.exceptions.Timeout as timeout:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[TIMEOUT ERROR]", Fore.RED+str(timeout))
                self.lock.release()
                continue
            except requests.exceptions.RequestException as err:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[ERROR]", Fore.RED+str(err))
                self.lock.release()
                continue
            except requests.exceptions.ProxyError as proxErr:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[PROXY ERROR]", Fore.RED+str(proxErr))
                self.lock.release()
                self.chooseProxy()
                continue
            
            
    def addWatcher(self):
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"Adding Watcher {self.email}")
        self.lock.release()
        
        while True:
            try:
        
                request = self.s.post(data.signIn_URL,headers=data.Headers.signIn, timeout=12, allow_redirects=False)
                
                return
            
            except requests.exceptions.ConnectionError as connectionerror:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[CONNECTION ERROR]", Fore.RED+str(connectionerror))
                self.lock.release()
                continue
            except requests.exceptions.Timeout as timeout:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[TIMEOUT ERROR]", Fore.RED+str(timeout))
                self.lock.release()
                continue
            except requests.exceptions.RequestException as err:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[ERROR]", Fore.RED+str(err))
                self.lock.release()
                continue
            except requests.exceptions.ProxyError as proxErr:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[PROXY ERROR]", Fore.RED+str(proxErr))
                self.lock.release()
                self.chooseProxy()
                continue