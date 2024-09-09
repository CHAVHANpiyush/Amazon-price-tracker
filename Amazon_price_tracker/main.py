import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL="https://www.amazon.in/Sony-Bravia-inches-Google-KD-55X74L/dp/B0C1HCJVT5/ref=sr_1_4?crid=1K62DU6PX6CGK&dib=eyJ2IjoiMSJ9.HLZdBbMmx6ihTUQDo8oJxqQlaL4nfG6tdSJeNZRfdLTJ4RlLlMHMxrLf65FgAguVsG5uQk8BKs5pZn0c_oXJxSsmilnf5ggtV1Er6ddvSW3ZdMF-ECbjJLxsbgqUD8Mi1jn3XhJBvJ0nzLV3bgtCs29lMjmZBy9yPfCfmS8lbbNom9_YqVG-oQLUH-wrhpYgS18RY8FkAZaN-PeAEejAO6b3dZDTgmq4mI-LxC-bo0k.TT1pb6opjszcSoUBWh2RrS7uZik2RSjhOdbypG8BOwY&dib_tag=se&keywords=sony+tv&qid=1720272858&sprefix=sony%2Caps%2C199&sr=8-4"

header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15",
    "Accept-Language":"en-IN,en-GB;q=0.9,en;q=0.8",
}
response =requests.get(url=URL,headers=header)
soup=BeautifulSoup(response.text,"lxml")
price=float((soup.find(name="span",class_="a-price-whole").getText()).replace(",","").strip('.'))
name=soup.find(name="span",id="productTitle").getText().strip(" ")

my_mail="hisenbergjimmy@gmail.com"
password="dgzcrxlqvhrupwtl"
my_price=56000

message=f"Subject:Amazon Price Alert\n\n{name} is now {(soup.find(name='span',class_='a-price-whole').getText())}{URL}"
if price<=my_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail,password=password)
        connection.sendmail(from_addr=my_mail,to_addrs="piyushchavhan847@gmail.com",msg=message.encode('utf-8'))
