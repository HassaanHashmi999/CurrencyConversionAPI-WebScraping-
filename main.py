import requests
import sys
chk=0
cka2=0
cka3=0
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
date=arg1
to_currency=arg3.upper()
from_currency=arg2.upper()



respons = requests.get(
        "https://api.frankfurter.app/currencies")
    

for link in respons.json():
    if(from_currency==link):
        chk+=1
        cka2=1
    if(to_currency==link):
        chk+=1
        chka3=1
if(len(sys.argv)>3 and len(sys.argv)<0):
    print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")


if(chk==2 and date[4]=="-" and int(date[0:4])<2023 and int(date[5:7])<13 and int(date[8:10])<32):
      
    response = requests.get(
        f"https://api.frankfurter.app/{date}?amount={1.0}&from={from_currency}&to={to_currency}")

    print(f"{1.0} {from_currency} was {response.json()['rates'][to_currency]} {to_currency}")

    response = requests.get(
        f"https://api.frankfurter.app/{date}?amount={1.0}&from={to_currency}&to={from_currency}")

    print(f"{1.0} {to_currency} was {response.json()['rates'][from_currency]} {from_currency}")

elif(chk<2 and cka2==0):
    print(arg2+"is not a valid currency code")

elif(chk<2 and cka3==0):
    print(arg3+"is not a valid currency code")

if (cka2==0 and cka3==0):
    print(arg3+"and"+arg2+" are not a valid currency codes")



if(date[4]!="-" or int(date[0:4])>2022 or int(date[5:7])>12 or int(date[8:10])>31):
    print("Provided date is invalid")
