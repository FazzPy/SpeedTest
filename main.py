import random
import threading
import time
from colorama import Fore, init

init(autoreset=True)

words = ["selam", "naber", "nasılsın", "tamam"]

print(Fore.RED + "Hızlı Yazma Testi | Made By Fazz | Süre : 60 Saniye | Başla!")

def basla():
    global true
    global false
    true = 0
    false = 0
    while True:
        item = random.choice(words)
        print(Fore.BLUE +f"Kelime : {item}")
        enter = input("Kelime Giriniz : ")
        if enter == item:
            true = true+1
            print(Fore.GREEN +"Doğru! Geçen Süre : ", sec)
        else:
            false = false+1
            print(Fore.RED +"Yanlış! Geçen Süre : ", sec)
        
        if sec == 60:
            break

def time1():
    global sec
    sec = 0
    while sec < 60:
        sec = sec+1
        time.sleep(1)
        if sec == 60:
            print("Süre Bitti!")
            print("Doğru Sayısı : ",true)
            print("Yanlış Sayısı : ",false)
            input("Hızlı yazma testi bitmiştir!")

basla1 = threading.Thread(target=basla)
time2 = threading.Thread(target=time1)

basla1.start()
time2.start()
