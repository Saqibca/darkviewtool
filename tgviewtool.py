import requests,random,os
from user_agent import generate_user_agent
import webbrowser
headers={'user-agent': generate_user_agent()}
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
def like():
 user='qwertyuiopasdfghjklzxcvbnm'
 os.system('clear')
 urlm=input(f'{B}[+] Post URL(PUBLIC)==> {B}')
 urlm=urlm.split('/?')[0]
 urlm1=urlm
 id=8600
 fol=0
 def likes(id,fol):
  while True:
   url = 'https://smm.oodi.tk/api/v2'
   rn = str("".join(random.choice(user)for i in range(4)))
   urlm=(urlm1+'')
   data={'key':key,'action':'add','service':id,'link':urlm,'quantity':'1000'}
   whisper=requests.post(url,data=data)
   if 'You have active order with this link. Please wait until order being completed.' in whisper.text:
    print('[+] Wait The Past Order Complete')
   if '{"order":' in whisper.text:
    fol+=1000
    oid=str(whisper.json()['order'])
    print(f'{G}[√] Order ID {E}==> {B}{oid} {E}| {G}Send {E}==> {B}{fol} {G}TG VIEW\nTHIS TOOL IS MADE BY @DARKMETHOD_TOOL')
   if 'Invalid API key' in whisper.text:
    print(f'{E}[×] Wrong Key')
    print(f'{B}[=] DM TO BUY KEY==> {G}@L1L2Y')
    exit()
   if 'Bad link' in whisper.text:
    likes(id,fol)
   else:
    print(whisper.json())
 likes(id,fol)
os.system('clear')
webbrowser.open('https://t.me/+mbeAbZ2pi80wMmQ1')
key=input(f'{B}[+] ENTER TOOL KEY  ==> {G}')
url = 'https://smm.oodi.tk/api/v2'
data={'key':key,'action':'balance'}
whisper=requests.post(url,data=data,headers=headers)
if 'Invalid API key' in whisper.text:
 print(f'{E}[×] Wrong Key')
 print(f'{B}[=] DM TO BUY KEY ==> {G}@L1L2Y')
 exit()
else:
  os.system('clear')
  ch=input(f'''{B}[{G}01{B}] {S} TELEGRAM VIEW 
{B}[{G}INSTAGRAM{B}] {S}@GWXOM
{B}[{G}TELEGRAM{B}] {S}@L1L2Y
{B}[{G}TELEGRAM{B}] {S}@DARKMETHOD_TOOL
{G}[{B}${S}${G}] {G}Choose ==> ''')
  if ch == '1' or ch == '01':
   like()