from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            servisler_sms.append(attribute)

while True:
    system("cls||clear")
    print(f"""{Fore.RED}

                        88                       
                        ""                       
                                                 
8b,dPPYba,   ,adPPYba,  88 ,adPPYba,  ,adPPYba,  
88P'   `"8a a8"     "8a 88 I8[    "" a8P_____88  
88       88 8b       d8 88  `"Y8ba,  8PP"""""""  
88       88 "8a,   ,a8" 88 aa    ]8I "8b,   ,aa  
88       88  `"YbbdP"'  88 `"YbbdP"'  `"Ybbd8"'  

                    
                
                    by; Noise                                                                           

    """)

    try:
        menu = int(input(Fore.RED + "\n 1- SMS Gönder (Turbo)\n\n 2- Çıkış\n\n" + Fore.RED + " Seçim: "))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue

    if menu == 5:
        system("cls||clear")
        print(Fore.RED + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): " + Fore.WHITE, end="")
        tel_no = input()
        tel_liste = []

        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Telefon numarası girmediğiniz için işlem iptal edildi.")
            sleep(3)
            continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(Fore.RED + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.WHITE, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.RED + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: " + Fore.WHITE, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.RED + "Kaç saniye aralıkla göndermek istiyorsun: " + Fore.WHITE, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        if kere is None:
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in servisler_sms:
                    exec("sms." + attribute + "()")
                    sleep(aralik)
        else:
            for i in tel_liste:
                sms = SendSms(i, mail)
                while sms.adet < kere:
                    for attribute in servisler_sms:
                        if sms.adet == kere:
                            break
                        exec("sms." + attribute + "()")
                        sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
        input()

    elif menu == 1:
        system("cls||clear")
        print(Fore.RED + "Telefon numarasını başında '+90' olmadan yazınız: " + Fore.WHITE, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.RED+ "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): " + Fore.WHITE, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.")
            sleep(3)
            continue

        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(getattr(send_sms, attribute))
                        for attribute in servisler_sms
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)

    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break