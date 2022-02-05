# Hayo mau apa lu?
# record kah cil:v
import os,sys,time,requests
from time import sleep

# warna
h = "\033[0;32m";
b = "\33[0;36m";
m = "\33[31;1m";
p = "\33[37;1m";
k = "\33[33;1m";
c = "\e[0;36m";
u = "\e[0;35m";
os.system("clear")
print("   ")
print("""
\033[1;95m    ___   ___    __
\033[1;95m   / _/  / o |  / / •\033[1;95m Author : ERI
\033[1;95m  / _/  /  ,'  / /  •\033[1;95m Facebook : Eri Kdr
\033[1;95m /___/ /_/`_\ /_/   •\033[1;95m Github : Github.com/Eri-bit
""")
sleep(1)
print                                ("\33[37;1mIP:103.144.169.231")
print                                ("______________________________")
print                                ("\33[37;1mNomor Diawali Dengan 89539xxxx")
print                                ("______________________________")
print("""
[1].Gas Spam Sms
[0].Exit""")

# Run
nomor = input("Pilih : ")
print
# Pemasukan
nomor = input("[+] Nomor: ")
# Data Spam
req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
if 'terkirim' in req:
    print ("Spam Berhasil")
else:
    print ("Spam Gagal")
