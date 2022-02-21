import os
import sys
import names
import requests
import time
import random
import requests
import json
from pathlib import Path
from time import sleep
import datetime
from colorama import init
import threading
from bs4 import BeautifulSoup
from threading import Semaphore
from colorama import Fore, Back, Style
#import logging
import importlib.util
sys.path.append("Utilities")
import credentials
import get_proxy
import data
from requests import exceptions as requestsExceptions



init(autoreset=True)

class Gen:
    def __init__(self, EBAY:object, email, i ):
        self.lock = EBAY.lock
        self.sem = EBAY.sem
        self.email = email
        self.task = i
        self.s = requests.Session()
        self.start()
        
    def start(self):
        self.chooseProxy()
        self.task
        self.credentials()
        self.getSession()
        self.accountCreate()
        self.sem.release()
        return
    
    def credentials(self):
        self.firstName = names.get_first_name()
        self.lastName = names.get_last_name()
        self.password = credentials.password()

    def chooseProxy(self):
        self.s.proxies.update(get_proxy.get_proxies())
        return
    
    def getSession(self):
        
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.YELLOW}Getting Session {Fore.CYAN}{self.email}")
        self.lock.release()
        
        while True:
            try:
                request = self.s.get('https://signup.ebay.com/pa/crte?ru=https%3A%2F%2Fwww.ebay.com%2F',headers=data.Headers.getSession, timeout=12)
                
                soup = BeautifulSoup(request.text, 'html.parser')
                jayson = str(soup.find_all('script')[1]).strip()[59:-9]

                model = json.loads(jayson)
                self.csrfToken = model["model"]["modules"]["PARTIAL_REG_PERSONAL_EMAIL"]["form"]["submitCSRFToken"]

                self.ets = model["model"]["modules"]["PARTIAL_REG_PERSONAL_EMAIL"]["form"]["additionalFormData"]["ets"]

                self.ri = model["model"]["modules"]["PARTIAL_REG_PERSONAL_EMAIL"]["form"]["additionalFormData"]["ri"]
                
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
            
    def accountCreate(self):
        
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.YELLOW}Creating Account {Fore.CYAN}{self.email}")
        self.lock.release()
        
        while True:
            try:
                
                payload = {
                    "srt":self.csrfToken,
                    "firstname":self.firstName,
                    "lastname":self.lastName,
                    "Email": self.email,
                    "password": self.password,
                    "promotion":True,
                    "action":{
                        "name":"EMAIL_REG_FORM_SUBMIT"
                        },
                    "ri":self.ri,
                    "ets":self.ets
                    }
                
                this_file = Path(__file__)
                config_dir = this_file.parent.parent / 'Config'

                
                request = self.s.post(data.signup_URL ,json=payload, headers=data.Headers.accountCreate)
                #print(request.text)
                
                if "SUCCESS" in request.text:
                    session = json.dumps(self.s.cookies.get_dict())
                    f = open(config_dir / 'created_accounts.txt', "a")
                    f.write(f'{self.email}:{self.password}:{self.firstName}:{self.lastName}:{session} \n')
                    f.close()
                    self.lock.acquire()
                    print(Fore.LIGHTMAGENTA_EX + f"[Task: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.GREEN}Account Created Successfully {Fore.CYAN}{self.email}")
                    self.lock.release()
                    
                else:
                    error = json.loads(request.text)["fields"]
                    for i in error:
                        print(i["errorMessage"])
                    f = open(config_dir / 'failed_accounts.txt', "a")
                    f.write(f'{self.email} \n')
                    f.close()
                    self.lock.acquire()
                    print(Fore.LIGHTMAGENTA_EX + f"[Task: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.RED}Account Creation Failed {self.email}")
                    self.lock.release()
                    
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
        