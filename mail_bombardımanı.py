import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime. text import MIMEText
import sys
import os
import time

mesaj = MIMEMultipart()

#Gönderim yapılacak E-postada "Daha az güvenli uygulamalara izin ver" seçeneği açık olmalı

os.system("clear")
print("\033[0;32m")

gonderici = input("E-postanızı Girin: ")

sifre = input("Şifrenizi Girin: ")

mesaj["From"] = gonderici

mesaj["To"] = str(input("Alıcı'nın e-postasını girin: "))

mesaj["Subject"] = str(input("E-posta konusunu girin: "))

mesaj_içeriği = str(input("Metini girin: "))

miktar = int(input("Gönderilecek mail miktarını girin: "))

mesaj_gövdesi = MIMEText(mesaj_içeriği,"plain")

mesaj.attach(mesaj_gövdesi)


mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()

mail.login(gonderici,sifre)

a=1

if miktar > 200:
	print("\033[0;31mMail sayasının fazla olması maillerin gönderilme süresini arttıracaktır!\033[0;32m")

while a <= miktar:
	time.sleep(1.5)
	print("Mail", a, "gönderiliyor")
	a = a + 1
	mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

print("Mail Başarıyla Gönderildi...")

mail.close()
