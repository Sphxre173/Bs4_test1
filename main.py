import requests as rq
import bs4
import time as t
import os

os.system("clear")

url = "https://www.bnn.in.th/th/p/notebook/thin-light-notebook?gclid=CjwKCAjwg4SpBhAKEiwAdyLwvGR1LjROG0czsDNMshMUoLFCSlGvpHxAVJwgwOwekK_9LSiO5pRiQRoCD00QAvD_BwE"

stage1 = rq.get(url)

stage2 = bs4.BeautifulSoup(stage1.text, "html.parser")

stage3 = stage2.find_all("div", {"class" : "product-name"})
stage3ex = stage2.find_all("div", {"class" : "product-price"})
stage3spec = stage2.find_all("div", {"class" : "product-short-attribute"})

#n = name 
#p = price
#s = spec

counter = 1

for n, p, s in zip(stage3, stage3ex, stage3spec):
  nprocessed = n.get("title")
  pprocessed = p.text.strip("")
  sprocessed = s.text
  print(f"{str(counter)}. Name : {nprocessed} \nPrice: {pprocessed} \nSpec : {sprocessed} ")
  print("-------------------------------------------------")
  t.sleep(0.3)
  counter += 1

with open("Lite_Laptop_Bnn.txt", "w") as file:
  counter = 1
  for n, p, s in zip(stage3, stage3ex, stage3spec):
    nprocessed = n.get("title")
    pprocessed = p.text.strip("")
    sprocessed = s.text

    
    file.write(f"""{str(counter)}. Name : {nprocessed} \nPrice: {pprocessed} \nSpec : {sprocessed} \n ------------------------------------------------- \n""")

    
    t.sleep(0.3)
    counter += 1

#<div data-v-a391266e="" title="โน๊ตบุ๊ค Asus Zenbook 14 OLED UM3402YA-KM537WS Jade Black" class="product-name">