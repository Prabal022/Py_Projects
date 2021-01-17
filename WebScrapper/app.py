import requests
from bs4 import BeautifulSoup
import pandas

headers = {
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
                                  headers=headers)
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"propertyRow"})
page_nr=soup.find_all("a",{"class":"Page"})[-1].text
#print(page_nr,"number of pages were found")


base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
l = []

for page in range(0,int(page_nr)*10,10):
    #print(base_url+str(page)+".html")
    r = requests.get(base_url+str(page)+".html",headers=headers)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    
    
    for item in all:
        d = {}
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace(
            "\n", "").replace(" ", "")
        try:
            d["Address"] = (item.find_all(
                "span", {"class": "propAddressCollapse"})[0].text)
        except:
            d["Address"] = None
        try:
            d["Locality"] = item.find_all(
                "span", {"class": "propAddressCollapse"})[1].text
        except:
            d["Locality"] = None

        try:
            d["Beds"] = item.find("span", {"class": "infoBed"}).text
        except:
            d["Beds"] = None

        try:
            d["Area"] = item.find("span", {"class": "infoSqFt"}).text
        except:
            d["Area"] = None

        try:
            d["Full Bath"] = item.find(
                "span", {"class": "infoValueFullBath"}).text
        except:
            d["Full Bath"] = None

        try:
            d["Half Bath"] = item.find(
                "span", {"class": "infoValueHalfBath"}).text
        except:
            d["Half Bath"] = None

        for col_g in item.find_all("div", {"class": "columnGroup"}):
            for feat_group, feat_name in zip(col_g.find_all("span", {"class": "featureGroup"}),
                                             col_g.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feat_group.text:
                    try:
                        d["Lot Size"] = feat_name.text
                    except:
                        d["Lot Size"] = None
        l.append(d)

df1 = pandas.DataFrame(l)
df1.to_csv("Output_ex_code.csv")