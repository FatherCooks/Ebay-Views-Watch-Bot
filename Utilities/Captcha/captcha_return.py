import FB_captcha
import random

class captcha:
    def __init__(self,):
        self.twoCaptcha_v2 = FB_captcha.v2.twoCaptcha()
        self.anticCaptcha_v2 = FB_captcha.v2.antiCaptcha()
    
        def cap():
            choice = random.choice(self.twoCaptcha_v2 , self.anticCaptcha_v2)
            return choice

captcha()
        