import time
import html
import requests
import json
import concurrent.futures

from bs4 import BeautifulSoup
from requests.models import codes


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
Captchasite = 'http://2captcha.com/in.php?key=[YOUR 2CAP API KEY HERE]&method=userrecaptcha&googlekey=6LcYLioTAAAAAHRLLz3RBHBw2IkkjzocVqCL1uCt&json=1&pageurl=https://www.pokemon.com/us/pokemon-trainer-club/enter-codes'

sitekey = '6LcYLioTAAAAAHRLLz3RBHBw2IkkjzocVqCL1uCt'


def CaptchaSolver(name):
    global captcha_token
    print(f'[Thread {name}] Retrieving Session...')
    r = requests.post(Captchasite, headers=headers)
    print(f'[Thread {name}] Session Retrieved...')
    captcha_ID = json.loads(r.text)
    captcha_ID = captcha_ID['request']
    while True:
        r = requests.get(f'http://2captcha.com/res.php?key=[YOUR 2CAP API KEY HERE]&action=get&id={captcha_ID}&json=1', headers=headers)
        captcha_status = json.loads(r.text)
        status = captcha_status['status']
        if status == 0:
            print(f'[Thread {name}] AWAITING CAPTCHA TOKEN')
        elif status == 1:
            print(f'[Thread {name}] CAPTCHA TOKEN RETRIEVED')
            captcha_token = captcha_status['request']
            r.close()
            break
    print(captcha_token)



def Codechecker():
    with requests.Session() as s:
        print(f'Retrieving Login Token...')
        r = s.get('https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin', headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        soup = soup.find('form', {'id':'login-form'})
        soup = soup.find('input', {'name':'lt'})
        LoginID = soup['value']
        print(f'Successfully Retrieved Login Token... [{LoginID}]')
        UserCredentials = {
            'lt': LoginID,
            'execution': 'e1s1',
            '_eventId': 'submit',
            'username': 'YOUR POKEMON TRAINER CLUB USERNAME HERE',
            'password': 'YOUR POKEMON TRAINER CLUB PASSWORD HERE',
            'Login': 'Log In'
        }
        #print(f'Retrieved Login Token! | [{LoginID}]')
        print(f'Logging Into Account...')
        r = s.post('https://sso.pokemon.com/sso/login?locale=en&service=https://www.pokemon.com/us/pokemon-trainer-club/caslogin', headers=headers, data=UserCredentials)
        print(r)
        print(f'Successfully Logged In...')
        r = s.get('https://www.pokemon.com/us/pokemon-trainer-club/enter-codes', headers=headers)
        print(r)

        print(f'Preparing Codes For Submission...')
        codes = ['INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE', 'INSERT PTCGO CODES HERE']

        for code in codes:
            data = {
                'code': code,
                'g-recaptcha-response': captcha_token
            }
            
            r = s.post('https://www.pokemon.com/us/pokemon-trainer-club/verify_code/', headers=headers, data=data)
            info = json.loads(r.text)
            #print(f'Submitting Code... [{info}]')
            try:
                print(f'Submitting Code... [{info}] {html.unescape(info["coupon_title"])}')
            except KeyError:
                print(f'Submitting Code... [{info}]')
            if str(r) == '<Response [400]>':
                print(f'Error Submitting Code... [{r.text}]')
            #print(r.text)
        s.close()
def Main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(CaptchaSolver, range(1, 3))

if __name__ == "__main__":
    CaptchaSolver('MAIN')
    Codechecker()
    


