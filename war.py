import requests,sys
from time import sleep
from datetime import datetime, timedelta
import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
def banner():
 banner = f"""
\033[1;32m╔═══════════════════════════════╗
\033[1;32m║   \033[1;31mFix Tool : \033[1;33mGIRA CTEE💓
\033[1;32m║═══════════════════════════════║
\033[1;32m║   \033[1;31mLiên Hệ fb : \033[1;33m 🌊 𝐕ă𝐧 𝐍𝐠𝐡ĩ𝐚🍂 
\033[1;32m╚═══════════════════════════════╝
\033[1;37mLưu ý khỉ sử dụng nhé.!

"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
os.system("cls" if os.name == "nt" else "clear")
banner()

print(" \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("\033[1;31mAdmin: \033[1;33mGIRA CTEE💕")                                     
print("\033[1;35mContact Support: https://www.facebook.com/profile.php?id=61558228388873&mibextid=ZbWKwL")
print("\033[1;35mGIRA CTEE Decode - Decode Liên Hệ fb : 🌊 𝐕ă𝐧 𝐍𝐠𝐡ĩ𝐚🍂  ")
print("- \033[1;37m - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(" \033[1;37m╔═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức Năng [1] \033[1;36mNhây Có Dấu by:gira💗")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➢Chức năng [2] \033[1;36mNhây Không Dấu")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➣Chức năng [3] \033[1;36mNhây Réo Tên | Recode by 𝐕ă𝐧 𝐍𝐠𝐡ĩ𝐚🍂 |")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➢Chức năng [4] \033[1;36mTreo Spam Messenger | để 10s hoặc 20s |")
print("\033[1;37m ║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [5] \033[1;36mNhây Code Lag")                               
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➢Chức năng [6] \033[1;36mTreo Sớ")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➣Chức năng [7] \033[1;36mNhây Dis")
print(" \033[1;37m╚═════════════════════════════════════════════════════════════")
chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;33m'))

if chon == 1 :

	exec(requests.get('https://932ea2d3f21f47ffb8d17441dce80c75.api.mockbin.io/').text)

if chon == 2 :

	exec(requests.get('https://5ceaa4d7986642e4a87a05b39adbdd37.api.mockbin.io/').text)
if chon == 3 :

	exec(requests.get('https://5ac08b8391b24702afa3c8cda4265e0a.api.mockbin.io/').text)

if chon == 4 :

	exec(requests.get('https://c739f07abdbd477da4b14c6537b340c0.api.mockbin.io/').text)

if chon == 5 :

	exec(requests.get('https://f8e00f70e4ec4195950d6634f90ddbb8.api.mockbin.io/').text)

if chon == 6 :

	exec(requests.get('https://50fac8d46b1b44ae9cee410435346e56.api.mockbin.io/').text)

if chon == 7 :

	exec(requests.get('https://03d4c2c994974217b8820a11c8301420.api.mockbin.io/').text)

	print (" Sai Lựa Chọn ")

	exit()