import requests
from bs4 import BeautifulSoup

l=list()
g=list()
o={}
k={}
fac=[]
fac_arr=[]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

target_url = "https://www.booking.com/hotel/us/royal-lotus.html?checkin=2023-12-28&checkout=2023-12-29&group_adults=2&group_children=0&no_rooms=1&selected_currency=USD"

resp = requests.get(target_url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')

o["name"]=soup.find("h2",{"class":"pp-header__title"}).text
o["address"]=soup.find("span",{"class":"hp_address_subtitle"}).text.strip("\n")
o["rating"]=soup.find("div",{"class":"d10a6220b4"}).text

fac=soup.find_all("div",{"class":"important_facility"})
for i in range(0,len(fac)):
    fac_arr.append(fac[i].text.strip("\n"))


ids= list()

targetId=list()
try:
    tr = soup.find_all("tr")
except:
    tr = None

for y in range(0,len(tr)):
    try:
        id = tr[y].get('data-block-id')

    except:
        id = None

    if( id is not None):
        ids.append(id)

print("ids are ",len(ids))


for i in range(0,len(ids)):

    try:
        allData = soup.find("tr",{"data-block-id":ids[i]})
        try:
            rooms = allData.find("span",{"class":"hprt-roomtype-icon-link"})
        except:
            rooms=None


        if(rooms is not None):
            last_room = rooms.text.replace("\n","")
        try:
            k["room"]=rooms.text.replace("\n","")
        except:
            k["room"]=last_room

        price = allData.find("div",{"class":"bui-price-display__value prco-text-nowrap-helper prco-inline-block-maker-helper prco-f-font-heading"})
        k["price"]=price.text.replace("\n","")


        
        
        
        g.append(k)
        k={}

    except:
        k["room"]=None
        k["price"]=None


l.append(g)
l.append(o)
l.append(fac_arr)
print(l)