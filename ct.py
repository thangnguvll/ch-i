from urllib.parse import quote
from secrets import compare_digest
import datetime
import os
import ssl
from urllib.parse import urlencode
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
import hashlib
import random
try:
    import base64
    from requests.exceptions import RequestException
    import requests
    import pystyle
    from concurrent.futures import ThreadPoolExecutor
    from faker import Faker
    from requests import session
    import concurrent.futures

except ImportError:
    import os
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install concurrent.futures")
    os.system("pip install base64")
import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import datetime
import requests,json
import uuid
import requests
from time import sleep
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from pystyle import Colors, Colorate, Write, Center, Add, Box
from time import sleep,strftime
import socket
from pystyle import *
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def runbanner(text, delay=0.001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033[1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]
random_color = random.choice(colors)
def idelay(o):
    while(o>0):
        o=o-1
        print(f"{trang}[{xanh_la}Chí Trọng{trang}] \033[1;33mV\033[1;34mu\033[1;35mi \033[1;32mL\033[1;33mò\033[1;34mn\033[1;35mg \033[1;36mC\033[1;33mh\033[1;34mờ {trang}[\033[1;35m.....""]""["+str(o)+"]""    ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{xanh_duong}Chí Trọng{trang}] \033[1;31mV\033[1;32mu\033[1;33mi \033[1;34mL\033[1;35mò\033[1;31mn\033[1;32mg \033[1;33mC\033[1;32mh\033[1;35mờ {trang}[\033[1;33m•{trang}....""]"f"{trang}[{xanhnhat}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{do}Chí Trọng{trang}] \033[1;32mV\033[1;33mu\033[1;34mi \033[1;35mL\033[1;36mò\033[1;33mn\033[1;34mg \033[1;35mC\033[1;31mh\033[1;32mờ {trang}[\033[1;35m••{trang}...""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{vang}Chí Trọng{trang}] \033[1;31mV\033[1;33mu\033[1;35mi \033[1;33mL\033[1;31mò\033[1;32mn\033[1;34mg \033[1;36mC\033[1;35mh\033[1;31mờ {trang}[\033[1;32m•••{trang}..""]"f"{trang}[{do}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{tim}Chí Trọng{trang}] \033[1;32mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;31mn\033[1;35mg \033[1;33mC\033[1;36mh\033[1;35mờ {trang}[\033[1;38m••••{trang}.""]"f"{trang}[{tim}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(1/6)
        print(f"{trang}[{hongnhat}Chí Trọng{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{vang}"+str(o)+f"{trang}]""     ",end='\r')
        time.sleep(0.1)
        print(f"{trang}[{xanhnhat}Phạm Chí Trọng{trang}] \033[1;31mV\033[1;34mu\033[1;36mi \033[1;32mL\033[1;34mò\033[1;32mn\033[1;35mg \033[1;36mC\033[1;34mh\033[1;32mờ {trang}[\033[1;33m•••••{trang}""]"f"{trang}[{xanh_la}"+str(o)+f"{trang}]""     ",end='\r')

chontool = """ \033[1;31m     _____                       _
\033[1;32m      \_   \_ __ ___  _ __  _   _| |___  ___
\033[1;33m       / /\/ '_ ` _ \| '_ \| | | | / __|/ _ \
\033[1;39m         /\/ /_ | | | | | | |_) | |_| | \__ \  __/
\033[1;35m    \____/ |_| |_| |_| .__/ \__,_|_|___/\___|
\033[1;36m                     |_| 

\033[1;39m┌──────────────────────── REAL ────────────────────────┐
\033[1;33m ➻ \033[1;39mDEV : Phạm Chí Trọng
\033[1;33m ➻ \033[1;39mFb : Phạm Chí Trọng
\033[1;33m ➻ \033[1;39mSupport : CT
\033[1;33m ➻ \033[1;39mBypass : Antiban tool
\033[1;33m ➻ \033[1;39mCoppy : Vip S1 sàn
\033[1;33m ➻ \033[1;39mTool Nhây                                       
\033[1;39m└────────────────────────────────────────────────────────┘
"""
clear()
runbanner(chontool)
idcanspam=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {hongnhat}Nhập id box:{do} ')
while True:
      ck=input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {tim}Nhập cookie:{hongnhat} ')
      try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={idcanspam}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        clear()
        break
      except:
        print(f'{do}Cookie sai!!')   
        runbanner(chontool)
params = {
      "icm": '1',
    }  
    
headers = {
      "Host":"mbasic.facebook.com",
      "content-length":"87",
      "content-type":"application/x-www-form-urlencoded",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "sec-fetch-site":"same-origin",
      "sec-fetch-mode":"navigate",
      "sec-fetch-user":"?1",
      "sec-fetch-dest":"document",
      "accept-encoding":"gzip, deflate, br",
      "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":ck,
    }
CAU_CHUI = [
"bọn t đến là m sít đao mà em",
"xem anh múa flo cân all ae m nè con th ú",
"Anh Đạp Đầu Lũ Cặn Bã Mxh Mà Con N gu ",
"bố m bá đến độ m phải ra tính sos để cầu cứu à",
"thằng ngâu bị anh hành cho ra b ã",
"úi úi đi nào con trai của cha",
"cay cú là b ú d ú bà già đấy à thằng l ồn",
"một khi anh đã m áu thì đừng hỏi bố cháu là ai",
"một khi đã có thai thì đừng hỏi ai là bố cháu",
"mày bị anh t ẩy chay mà thằng g ay",
"m thấy  tụ họp đông đủ là m hoảng loạn à",
"top những thằng đ ú ăn h ại mxh",
"top 1 kha gia huy",
"top 2 ng thuận",
"top 3 là m đó thằng kh ốn",
"cách những thằng đ ú đi war",
"cách 1 soi wall từ A đến Z",
"cách 2 thấy cái gì mình thua người ta thì cap lại th ủ d âm tinh thần",
"cách 3 núp clone lên top s ủa làm gì dám vác acc chính lên ý nói thằng ng thuận",
"đừng để anh bật mode ảo w ar lên không thôi m ẹ mày còn ch ết huống chi mày ",
"thằng ngâu hăng lên được không",
"mày đ ú à mà mới 15p đã thở hơi lên rồi",
"ồ nô thằng đú ngậm ngùi cayyyy đắng anh rồi",
"m xem b ướm ng già xong nhìn bư ớm gái trẻ cho dễ n ứng à",
"đúng thằng s úc sanh ngay cả b ím bà ngoại nó mà nó cũng không tha=))",
":)))",
"ơ sao vậy thằng lgbt",
"tk gay mạnh mẽ lên xem nào",
"bị anh nói trúng con chêm 2cm đen thui của m à",
"cố đi em zai",
"chăn chối cho sự n gu si t ứ chi k ém phát triển của m nào=))",
"cayyy rồi đấy à",
"nhanh v sao",
"anh chọc có tí mà muốn cắn l ưỡi tự x ác à",
"alo m sao đấy",
"ổn k",
"bất ổn level max à",
"rồi xong luôn",
"1p bất đồng cả đời bốc c ứt ăn à em",
"tội em v thằng nghịch t ử",
"thằng ngâu lừa thầy phản bạn bị ae bỏ rơi=))",
"cay cay cayyyy=)))",
"úi thằng g ay bất lực như con già nó rồi",
"s ủa 1 đoạn lofi cực chill anh nghe nào",
"alo alo bị t ch ửi đến lú à",
"t rủa m từ năm này qua tháng nọ mà",
"ê kêu m ẹ mày làm t phê đi rồi t tha cho",
"m ẹ mày là lô đỉnh sưởi ấm ciu t mà",
"bả con làm bồn chứa t inh cho t nữa đó",
"sáng m ẹ mày buscu t tối bả đi làm đix chứ đâu",
"log acc thay phiên dồn bố m à=)))",
"cố lên bố cân 50 60 thằng con được",
"mau nào",
"ơ ơ đừng có rụng mà",
"mày rụng mau vậy",
"chưa gì mà",
"sao chạy tư thế ch ó rồi:))",
"úi ơ kè nhỏ out rồi",
"tag nó lại coi",
"tao chưa cho phép nó chạy mà",
"sút lũ Cặn Bã Mxh Mà Con Ngu ",
"Mày win cha cái đi tk ngâu eyy ",
"Tốc độ bem anh đi con ngâu eyy ", 
"Mày phế như mẹ mày bị tao hi*p rồi bắn bỏ mà con chó eyy",
"Đừng Ngậm Đắng Nuốt Cay Tao Nha Con ngâu",
"Con Chó Cay Cha Rõ ",
"Óc Chó Ngồi Đọ Nhây Với Tao ",
"Mẹ Mày Bị Tao Đụ Lên Đỉnh Rồi ",
 "úi cn ngu óc cặc =))",
    "cn mẹ m k biết dạy m à eyy:))) ",
    "con chó m câm à :)?",
    "con chó ngu sợ tao run cầm cập mẹ r :))",
    "câm à con ngu:)))",
    "ngu ê :))",
    "úi cái con hôi háng:)))",
    "con mẹ chết dưới ao àa:)))",
    "địt cụ con lồn thâm dã man con ngan:)",
    "úi ",
"thằng bím đâm cha chém chú ",
  "alo alo",
" ngu=))",
  "con cặc:))",
  "ớt à:))🌶",
"chó sủa lofi đê😂",
"úi cái cn bẻm",
" nhà lá nhìn nó phèn v",
"lô cn bẻm cặc:))",
" có mẹ kh:)))?",
"à quên con  chó lmj có mẹ 😂😂",
"sủa chill đê",
",va ngu:))",
"chết cn già mày à $va:))",
"hình ảnh cn bẻm bị chà đạp:))",
"xúi cái cn giẻ rách:)))",
"tao có noti cn boài sợ tao:)))",
" tí bố cap úp tbg:))",
"akakakkakakaka:))))))",
" hãy cảm nhận nổi đauu:))))))",
"ngu sủa mau đi ơ",
" ôi mày bị cha xúc phạm kìa",
"óc ko cha ko mẹ bị khinh thường",
"m có cha sanh mẹ đẻ ra chỉ để bị t sỉ vả thôi hả",
"mày cay tao mà ",
"đĩ ngu bị cha chửi mà con ",
"mày run sợ trước tao mà ",
"con bẻm sợ t mà",
"nhìn mày đơ vậy ",
"bú đá quá 180p àk",
"nhìn gà ỉa chảy",
"bị chửi t mà sợ t mày",
" câm hận tao lắm",
"xem anh múa flo cân all ae m nè con th ú",
"Anh Đạp Đầu Lũ Cặn Bã Mxh Mà Con N gu ",
"bố m bá đến độ m phải ra tính sos để cầu cứu à",
"thằng ngâu bị anh hành cho ra b ã",
"úi úi đi nào con trai của cha",
"cay cú là b ú d ú bà già đấy à thằng l ồn",
"một khi anh đã m áu thì đừng hỏi bố cháu là ai",
"một khi đã có thai thì đừng hỏi ai là bố cháu",
"mày bị anh t ẩy chay mà thằng g ay",
"top những thằng đ ú ăn h ại mxh",
"top 1 kha gia huy",
"top 2 ng thuận",
"top 3 là m đó thằng kh ốn",
"cách những thằng đ ú đi war",
"cách 1 soi wall từ A đến Z",
"cách 2 thấy cái gì mình thua người ta thì cap lại th ủ d âm tinh thần",
"cách 3 núp clone lên top s ủa làm gì dám vác acc chính lên ý nói thằng ng thuận",
"đừng để anh bật mode ảo w ar lên không thôi m ẹ mày còn ch ết huống chi mày ",
"thằng ngâu hăng lên được không",
"mày đ ú à mà mới 15p đã thở hơi lên rồi",
"ồ nô thằng đú ngậm ngùi cayyyy đắng anh rồi",
"m xem b ướm ng già xong nhìn bư ớm gái trẻ cho dễ n ứng à",
"đúng thằng s úc sanh ngay cả b ím bà ngoại nó mà nó cũng không tha=))",
":)))",
"ơ sao vậy thằng lgbt",
"bị anh nói trúng con chêm 2cm đen thui của m à",
"cố đi em zai",
"chăn chối cho sự n gu si t ứ chi k ém phát triển của m nào=))",
"cayyy rồi đấy à",
"nhanh v sao",
"anh chọc có tí mà muốn cắn l ưỡi tự x ác à",
"alo m sao đấy",
"ổn k",
"bất ổn level max à",
"rồi xong luôn",
"1p bất đồng cả đời bốc c ứt ăn à em",
"tội em v thằng nghịch t ử",
"thằng ngâu lừa thầy phản bạn bị ae bỏ rơi=))",
"cay cay cayyyy=)))",
"úi thằng g ay bất lực như con già nó rồi",
"s ủa 1 đoạn lofi cực chill anh nghe nào",
"alo alo bị t ch ửi đến lú à",
"t rủa m từ năm này qua tháng nọ mà",
"ê kêu m ẹ mày làm t phê đi rồi t tha cho",
"m ẹ mày là lô đỉnh sưởi ấm ciu t mà",
"bả con làm bồn chứa t inh cho t nữa đó",
"sáng m ẹ mày buscu t tối bả đi làm đix chứ đâu",
"log acc thay phiên dồn bố m à=)))",
"cố lên bố cân 50 60 thằng con được",
"mau nào",
"ơ ơ đừng có rụng mà",
"mày rụng mau vậy",
"chưa gì mà",
"sao chạy tư thế ch ó rồi:))",
"úi ơ kè nhỏ out rồi",
"tag nó lại coi",
"tao chưa cho phép nó chạy mà",
"AECT sút lũ Cặn Bã Mxh Mà Con Ngu ",
"Mày win cha cái đi tk ngâu eyy ",
"Tốc độ bem anh đi con ngâu eyy ", 
"Mày phế như mẹ mày bị tao hi*p rồi bắn bỏ mà con chó eyy",
"Đừng Ngậm Đắng Nuốt Cay Tao Nha Con ngâu",
"Con Chó Cay Cha Rõ ",
"Óc Chó Ngồi Đọ Nhây Với Tao ",
"Mẹ Mày Bị Tao Đụ Lên Đỉnh Rồi ",
 "úi cn ngu óc cặc =))",
    "cn mẹ m k biết dạy m à eyy:))) ",
    "con chó m câm à :)?",
    "con chó ngu sợ tao run cầm cập mẹ r :))",
    "câm à con ngu:)))",
    "ngu ê :))",
    "úi cái con hôi háng:)))",
    "con mẹ chết dưới ao àa:)))",
    "địt cụ con lồn thâm dã man con ngan:)",
    "úi ",
"thằng bím đâm cha chém chú ",
  "alo alo",
" ngu=))",
  "con cặc:))",
  "ớt à:))🌶",
"chó sủa lofi đê😂",
"úi cái cn bẻm",
" nhà lá nhìn nó phèn v",
"lô cn bẻm cặc:))",
" có mẹ kh:)))?",
"à quên con  chó lmj có mẹ 😂😂",
"sủa chill đê",
",va ngu:))",
"chết cn già mày à :))",
"hình ảnh cn bẻm bị chà đạp:))",
"xúi cái cn giẻ rách:)))",
"tao có noti cn boài sợ tao:)))",
" tí bố cap úp tbg:))",
"akakakkakakaka:))))))",
" hãy cảm nhận nổi đauu:))))))",
"ngu sủa mau đi ơ",
" ôi mày bị cha xúc phạm kìa",
"óc ko cha ko mẹ bị khinh thường",
"m có cha sanh mẹ đẻ ra chỉ để bị t sỉ vả thôi hả",
"mày cay tao mà ",
"đĩ ngu bị cha chửi mà con ",
"mày run sợ trước tao mà ",
"con bẻm sợ t mà",
"nhìn mày đơ vậy ",
"bú đá quá 180p àk",
"nhìn gà ỉa chảy",
"bị chửi t mà sợ t mày",
" câm hận tao lắm",
"đừng cay tao nữa nha ",
"con chó bú cứt kkkkkk",
"bị tao xúc phạm ko biết nhục à ",
"oan ức ko ",
"thù ghét tao à ",
"con chó làm mẫu sủa cha mày coi tí đi ",
"con 3d dái bộng",
"bị tao chửi rung cặc mà đk ",
"con chó ỉa cứt chảy mà ",
"nào mày ăn dc tao thế ",
"sử dụng ngôn từ gây sát thương đi mò ",
"có sát thương chí mạng ko ",
"cần buil cho m cây thánh kiếm k vậy em",
"chứ nhìn m s ủa như phủi bụi v",
"m nhà lá dk ",
"nào m ở biệt thự như bố vậy ",
"cay lắm rồi à ",
"cạn ngôn rồi kìa ",
"mẹ mày béo như heo vậy ",
"thằng nghịch tử sao m giết cha m thế ",
"m nỡ đút con cặc vào cái lồn hết tinh dịch của má m vậy ",
"mày bị t chửi chỉ biết nghe thôi hả ",
"yếu kém đòi va tao vậy ",
"coi nó đỏ mặt vì cay đắng kkk ",
"🤣 tội mà ghê á trơi",
"cay dữ thần thiên địa đk thằng n gu",
"bố là ác quỷ fefe nè ",
"bố đứng s1 bảng xếp hạng liqi mà",
"t bắn shot gun nát đầu bà nội m luôn đó tin không ",
"m ăn cứt gà xong chà vô mặt í ",
"mặt m dính đầy cứt gà lau dùm t đi ơi trông bẩn vcl",
"phèn thì né xa t ra đi ",
"mày vs lũ bạn mày ăn dc t ko đó ",
"1 lũ phèn v ",
"hạ đẳng thế làm j có tuổi với anh vậy ",
"ngu ra oai xong bị t sút bại quê ko ",
"con chó bú cứt tao mà $va",
"sao m hửi đít t khen thơm tho v",
"thằng đ ú mày chưa nghe danh tao à ",
"tao nói con nó đã xấu thêm cái gà mà sĩ gái",
"tao đấng sàn war mà ",
"nghèo có dám kèo nhây 500 củ như a ko",
"Anh Em Chí Trọng Bá Nhất Nhì cái sàn này mà",
"c hó ng u vạn kiếp ko ăn dc tao",
"thằng ó c c hó bị t sỉ nh ục đến méc mẹ",
"cay tao à thì bú dá i th ằng c ha m đê",
"m tính lên ăn hôi à ",
"gặp t là m ăn hôi bất thành rồi con",
"ức chế tao lắm rồi mà con c hó ",
"thằng boài sủa chill đi",
"con h eo mập cấm m ăn cám xú",
"đọ tiền phát ko ",
"phèn thì câm nha ai cho m lên tiếng vậy",
"thằng ó c ch ó cay cha lắm dk",
"m đẹp bằng vk tao ko v ",
"đọ danh vs bố kh kkk",
"lên đê thằng ăn c ứt c hó thay cơm",
"t đếm 123 m chưa lên là t hi ếp mẹ m gi ết cha m đó",
"m bị tao ch ửi đến off mxh luôn r hả",
"sao m có tuổi ăn tao đó ",
"tuổi lờ à con",
"t ra hiệu lệnh m mới dc chạy nha con ngu óc c ứt ",
"bị tao bón hành ngập mồm mà ",
"n gu đối diện vs nghịch cảnh",
"m câm = t win đó ",
"nhắm win được tao không ",
"mày gà vcl luôn",
"tao là hw mà ",
"lè lưỡi ra điếm chân bố mày đê ",
"súc v ật cay tím tái cơ thể hết trơn rồi hả ",
"thằng cặk óc chó vãi c ứt",
"thấy tao là hw nên làm thân hả :)) ",
  "cay cú đổ mặt rồi kìa thằng ng u ",
"batman cũng onl mxh hả hả ",
"thằng chó × thằng gay là mày đó",
"thằng đầu đinh ôm hận tao hả ",
"tao bá đạo vcl ",
"mày ăn c ứt tao cho khôn nè ",
"êi thằng không cha không mẹ sao không hăng nữa êi ",
"mới có tí xíu đã đuối rồi à",
"gặp tao nên tay chân mày run rẩy dk ",
"sợ tao rồi thì nói nhe ",
"thằng ó c lồ n cay cú tao suốt đời",
"thằng con cặk ẳ ng nhanh nhẹn lên êi ",
"chậm chạp vãi ",
"thấy tao mạnh quá nên mày quỳ lạy van xin à ",
"cho mày 3s để gg á ",
"1 ",
"2",
"3",
"mày ăn cứt tao không ",
"mãnh mẽ lên xem nào thằng ngu ",
"đàn ông hay đàn bà mà yếu ớt quá dị hả ",
"hăng hái lên xem nào ",
"mới có nhiu đó mà mày đuối sức rồi hả ",
"rồi trình như vậy nào mới bằng tao áa",
"mẹ mày ốm liệt giường sao mày ảo ửa dạ ",
"mày b ất hiếu vậy thằng l ồn ",
"thằng đần bất hiếu vcl",
"đang ch ửi nhau mà mày hết oxy hả ",
"nhìn mày trong như mấy thằng sì ke á ",
"thằng ó c bư ớm nghiện à",
"thằng ng u nghiện ma túy bị tao phát hiện nên ôm hận tao hả ",
"cố gằng bằng tao đê ",
"mặt lồn cay cú tao đỏ con cặk ",
"xạo l ồn ăn c ứt tao nhe thằng ch ó ",
"alo alo ",
"sủa lên đê em êi ",
"bị tao chọc tới mách mẹ à ",
"đừng cay tao nữa nha ",
"con chó bú cứt kkkkkk",
"bị tao xúc phạm ko biết nhục à ",
"oan ức ko ",
"thù ghét tao à ",
"con chó làm mẫu sủa cha mày coi tí đi ",
"con 3d dái bộng",
"bị tao chửi rung cặc mà đk ",
"con chó ỉa cứt chảy mà ",
"nào mày ăn dc tao thế ",
"sử dụng ngôn từ gây sát thương đi mò ",
"có sát thương chí mạng ko ",
"cần buil cho m cây thánh kiếm k vậy em",
"chứ nhìn m s ủa như phủi bụi v",
"m nhà lá dk ",
"nào m ở biệt thự như bố vậy ",
"cay lắm rồi à ",
"cạn ngôn rồi kìa ",
"mẹ mày béo như heo vậy ",
"thằng nghịch tử sao m giết cha m thế ",
"m nỡ đút con cặc vào cái lồn hết tinh dịch của má m vậy ",
"mày bị t chửi chỉ biết nghe thôi hả ",
"yếu kém đòi va tao vậy ",
"coi nó đỏ mặt vì cay đắng kkk ",
"🤣 tội mà ghê á trơi",
"cay dữ thần thiên địa đk thằng n gu",
"bố là ác quỷ fefe nè ",
"bố đứng s1 bảng xếp hạng liqi mà",
"t bắn shot gun nát đầu bà nội m luôn đó tin không ",
"m ăn cứt gà xong chà vô mặt í ",
"mặt m dính đầy cứt gà lau dùm t đi ơi trông bẩn vcl",
"phèn thì né xa t ra đi ",
"m phế phẩm vcl v em",
"nhây có tí mà m thở hơi lên rồi àk",
"yếu đuối v thằng đàn bà",
"mày vs lũ bạn mày ăn dc t ko đó ",
"1 lũ phèn v ",
"hạ đẳng thế làm j có tuổi với anh vậy ",
"ngu ra oai xong bị t sút bại quê ko ",
"con chó bú cứt tao mà $va",
"sao m hửi đít t khen thơm tho v",
"thằng đ ú mày chưa nghe danh tao à ",
"tao nói con nó đã xấu thêm cái gà mà sĩ gái",
"tao đấng sàn war mà ",
"nghèo có dám kèo nhây 500 củ như a ko",
"Anh Em Chí Trọng Bá Nhất Nhì cái sàn này mà",
"c hó ng u vạn kiếp ko ăn dc tao",
"thằng ó c c hó bị t sỉ nh ục đến méc mẹ",
"cay tao à thì bú dá i th ằng c ha m đê",
"m tính lên ăn hôi à ",
"gặp t là m ăn hôi bất thành rồi con",
"ức chế tao lắm rồi mà con c hó ",
"thằng boài sủa chill đi",
"con h eo mập cấm m ăn cám xú",
"đọ tiền phát ko ",
"phèn thì câm nha ai cho m lên tiếng vậy",
"thằng ó c ch ó cay cha lắm dk",
"m đẹp bằng vk tao ko v ",
"m bá như bố k",
"đọ danh vs bố kh kkk",
"lên đê thằng ăn c ứt c hó thay cơm",
"t đếm 123 m chưa lên là t hi ếp mẹ m gi ết cha m đó",
"m bị tao ch ửi đến off mxh luôn r hả",
"cố đi m",
"m kém cỏi v",
"m có gì mạnh k",
"trổ tài t xem",
"m úi phát đi em",
"úi úi đi nào",
"m sao v",
"chưa gì đã đuối",
"m đú 2024 àk",
"mới vào sàn 10p à",
"tk gà này",
"sao m có tuổi ăn tao đó ",
"tuổi lờ à con",
"t ra hiệu lệnh m mới dc chạy nha con ngu óc c ứt ",
"bị tao bón hành ngập mồm mà ",
"n gu đối diện vs nghịch cảnh",
"m câm = t win đó ",
"nhắm win được tao không ",
"mày gà vcl luôn",
"tao là hw mà ",
"lè lưỡi ra điếm chân bố mày đê ",
"súc v ật cay tím tái cơ thể hết trơn rồi hả ",
"thằng cặk óc chó vãi c ứt",
"thấy tao là hw nên làm thân hả :)) ",
  "cay cú đổ mặt rồi kìa thằng ng u ",
"batman cũng onl mxh hả hả ",
"thằng chó × thằng gay là mày đó",
"thằng đầu đinh ôm hận tao hả ",
"tao bá đạo vcl ",
"mày ăn c ứt tao cho khôn nè ",
"êi thằng không cha không mẹ sao không hăng nữa êi ",
"mới có tí xíu đã đuối rồi à",
"gặp tao nên tay chân mày run rẩy dk ",
"sợ tao rồi thì nói nhe ",
"thằng ó c lồ n cay cú tao suốt đời",
"thằng con cặk ẳ ng nhanh nhẹn lên êi ",
"chậm chạp vãi ",
"thấy tao mạnh quá nên mày quỳ lạy van xin à ",
"cho mày 3s để gg á ",
"1 ",
"2",
"3",
"mày ăn cứt tao không ",
"mãnh mẽ lên xem nào thằng ngu ",
"đàn ông hay đàn bà mà yếu ớt quá dị hả ",
"hăng hái lên xem nào ",
"mới có nhiu đó mà mày đuối sức rồi hả ",
"rồi trình như vậy nào mới bằng tao áa",
"mẹ mày ốm liệt giường sao mày ảo ửa dạ ",
"mày b ất hiếu vậy thằng l ồn ",
"thằng đần bất hiếu vcl",
"đang ch ửi nhau mà mày hết oxy hả ",
"nhìn mày trong như mấy thằng sì ke á ",
"thằng ó c bư ớm nghiện à",
"thằng ng u nghiện ma túy bị tao phát hiện nên ôm hận tao hả ",
"cố gằng bằng tao đê ",
"mặt lồn cay cú tao đỏ con cặk ",
"xạo l ồn ăn c ứt tao nhe thằng ch ó ",
"alo alo ",
"sủa lên đê em êi ",
"bị tao chọc tới mách mẹ à ",
"úi khóc ỉa à",
"tội v thằng ngâu",
"alo chill phát",
"hăng đi mà",
"mạnh mẽ lên",
"tới sáng không con",
"mày biết sao mày không ăn được tao không",
"m với ngôi nhà khác nhau mà",
"nhà có cửa còn m thì không",
"tội m v",
"thằng ngâu ớt cái lờ bà già m à",
"hăng lên cho bố",
"m câm cái là bố cap noti à",
"nhanh tay lẹ chân lên đi mà thằng cẩu nô",
"úi mẹ m là nô lệ tình d ục cho bố mà",
"kkkkk run trái dứng àk",
"tk d ái đú",
"mau lên em ơi",
"mẹ m bị anh làm cho ch ết trong cơn phê chữ ê kéo dài mà",
"anh m bá vê lờ rồi",
"😂😂😂😂🤣🤣🤣"
"xem nó run bần bật kìa",
"tội v ",
"yếu mà bày đặc ra gió àk",
" úi nó chạy nhanh như ch ó chạy ngoài đồng kìa",
"m tính xông pha hiến m áu đấy ảk",
"đã v sao",
"thằng đ ú sĩ gái àk",
"thanh niên tập tành làm anh hùng giải cứu mĩ nhân:))",
"cứu nhầm mĩ đen r kìa m",
"=))",
"ảdu nó sốc đến nổi phải gào thét tên anh r",
"trầm cảm à em zai",
"sang chấn tâm lí cho cái pha sĩ gái à=))",
"đi thẳng vào lòng đất cmnr",
"tội dữ v sao",
"thằng óc c hó bị bệnh đao",
"co thắt cơ trym à",
"gồng cơ đ ít vận cơ m ông chi v",
"bị t ch ửi sợ đến nổi muốn ẻ ra quần à boa"
"sợ t cap noti win đến nổi nhịn ẻ àk",
"coi chừng phọt c ứt ra quần nha",
"t bán hành m ăn no luôn đc á",
"đụng t là mxh quay lưng với m liền",
"1p bất đồng",
"là cả đời m bốc c ứt ăn mà m",
"k có t thì m chỉ ăn c ứt",
"có t rồi t bón c ứt cho m ăn=)))",
"c ứt t mới ỉa luôn á còn trong bồn cầu kìa",
"đặc biệt thơm ngon ấy",
"để t cho m ăn nha",
"-)))",
"cay cú r kìa:)))",
"anh trêu có xíu mà nó sồn thấy ghê",
"thôi mà đừng sồn nữa",
"anh cho cục c ứt siêu to khổng lồ của bà tân vlog ngậm nè",
"ngoan ngoan k mếu mà",
"ngậm c ứt r nín đi em",
"ảdu nó ăn c ứt anh xong khen ngon bổ béo kìa",
"m chạy là anh win à:)))",
"gặp anh cái m rén ngang thế àk",
"A đi đến đâu bất bại đến đó mà",
"m hỏi A là gì sao=)))",
"đú như m sao biết Anh Em duy thang bất bại sàn",
"chú bé đần à🤣🤣🤣🤣",
"=))))",
"hài v dumo",
"cố đi ơ ơ",
"mau lên",
"hăng hái phát",
"thấy sự bá đạo của tụi bố cái rén ngang v",
"tk nghịch t ử đ âm cha gi ết m ẹ:)))",
"m s ủa phát đi",
"ớt àk",
"cố đi em zai",
"trụ đến 2030 với anh đi:)))",
"cái lờ bà già m",
"tk th ú đú",
"??? m yếu v à",
"chx gì hết mà",
" thằng đầu khất",
"đjt bà già luôn thằng ngâu này",
"ăn hại v",
"thằng phế phẩm này",
" chỉ biết ăn hôi thôi hả",
"cố chút nữa đi mà",
"gần đc r đó:)))",
"gần đc 30p r",
"cố đi=)))"
"sắp đc r:)))",
"đc danh đú 30p rớt đó",
"tội em:))",
"vừa vào sàn gặp bọn bố tắt nắng luôn",
"úi úi thằng nhỏ bại tướng khóc thảm chx kìa",
" đú war 2024 à nhóc "
"bọn t bá sàn này mà "
" m chui tu lon bà dà nhà m ra à "
" m nqu lắm cn chó ạ "
" sủa vài tiếng coi "
" co gõ phím nhìu vo e "
" cham vay "
" máy à "
" bot "
]
clear()
runbanner(chontool)
delay=int(input(f'\033[1;97m[\033[1;31m</>\033[1;97m] {xanhnhat}Nhập delay :{vang} '))
while True:
        try:
          ping = requests.get("https://www.google.com")
          if ping.status_code == 200:
            for nd in CAU_CHUI:
                data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{idcanspam}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"  
                response = requests.post("https://mbasic.facebook.com/messages/send/", params=params, headers=headers, data=data.encode('utf-8'))
                NOIDUNG = f"\033[1;39mChí Trọng\033[1;97m: {nd} \033[1;31m| \033[1;35mThành Công"
                print(f"{NOIDUNG}")
                idelay(delay)
        except Exception as e:
          print(f"{do}Wifi 999+")
          time.sleep(5)
else:
    print(f"{do}Vui lòng chọn đúng")