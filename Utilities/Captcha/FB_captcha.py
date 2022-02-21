
import requests
import time
import json
import sys
sys.path.append("Utilities")
from colorama import Fore, Back, Style
import datetime
import get_proxy
 
# Opening JSON file
f = open(r'D:\Scripts\Python\A Ma Maniere\Utilities\Captcha\credentials.json',)
global twoCaptchaKey, antiCaptchaKey, siteKey, website
# returns JSON object as
# a dictionary
data = json.load(f)

try:
    
    twoCaptchaKey = str(data['captcha'][0]['apiKey']['2CaptchaKey'])
    antiCaptchaKey = str(data['captcha'][0]['apiKey']['antiCaptchaKey'])
    siteKey = str(data['siteKey'])
    website = str(data['website'])
    #print(twoCaptchaKey)
   
except KeyError:
    print("[ERROR READING CREDENTIALS] Make sure you info in correct in credentials.json and try again")
   

class v2:
    pass
    def __init__(self,):
        self.proxies = get_proxy.get_proxies()
        self.s = requests.Session()
        self.s.proxies.update(self.proxies)
            
    
            

    def twoCaptcha():
        
        captcha_id = requests.post("http://2captcha.com/in.php?key="+twoCaptchaKey+"&method=userrecaptcha&googlekey="+siteKey+"&pageurl="+website,).text.split('|')[1]
        print(captcha_id)
        #print ("Request returned captcha ID:"+captcha_id)
        recaptcha_answer = requests.get("http://2captcha.com/res.php?key="+twoCaptchaKey+"&action=get&id="+captcha_id, ).text
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            #print (recaptcha_answer)#debug
            time.sleep(5)
            recaptcha_answer = requests.get("http://2captcha.com/res.php?key="+twoCaptchaKey+"&action=get&id="+captcha_id,).text       
        captcha = recaptcha_answer.split('|')[1]
        return captcha


    def antiCaptcha():
        print("anti captcha")
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            }

        data = { 
            "clientKey":antiCaptchaKey,
            "task": 
            {
                "type":"RecaptchaV2TaskProxyless",
                "websiteURL":website,
                "websiteKey":siteKey }}

        response = requests.post('https://api.anti-captcha.com/createTask', headers=headers, data=data, )
        while json.loads(response)["errorId"] > 0:
            response = requests.post('https://api.anti-captcha.com/createTask', headers=headers, data=data, )
            captcha = json.loads(response)["solution"]["gRecaptchaResponse"]

        return captcha



class v3:

    def antiCaptcha():
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            }
        
        data = {
            "clientKey":"YOUR_API_KEY",
            "task": { "type":"RecaptchaV3TaskProxyless",
            "websiteURL":"http://mywebsite.com/recaptcha/test.php",
            "websiteKey":"6Lc_aCMTAAAAABx7u2N0D1XnVbI_v6ZdbM6rYf16",
            "minScore": 0.9, "pageAction": "myverify", "isEnterprise": False } }
        response = requests.post('https://api.anti-captcha.com/createTask', headers=headers, data=data) 
        while json.loads(response)["errorId"] > 0: 
            time.sleep(10)
            response = requests.post('https://api.anti-captcha.com/createTask', headers=headers, json=data) 
            #captcha = json.loads(response)["solution"]["gRecaptchaResponse"]
            return 

    def twoCaptcha():

        captcha_id = requests.get("http://2captcha.com/in.php?key="+twoCaptchaKey+"&method=userrecaptcha&version=v3&action=verify&min_score=0.3&googlekey="+siteKey+"&pageurl="+website,).text.split('|')[1]
        #print(captcha_id)
        print ("Request returned captcha ID:"+captcha_id)
        print(Fore.BLUE + format(datetime.datetime.now()), Fore.YELLOW +"Waiting for Captcha!")
        recaptcha_answer = requests.get("http://2captcha.com/res.php?key="+twoCaptchaKey+"&action=get&id="+captcha_id, ).text
        while 'CAPCHA_NOT_READY' in recaptcha_answer:
            #print (recaptcha_answer)#debug
            time.sleep(5)
            recaptcha_answer = requests.get("http://2captcha.com/res.php?key="+twoCaptchaKey+"&action=get&id="+captcha_id,).text       
        captcha = recaptcha_answer.split('|')[1]
        #print(captcha)
        return captcha



