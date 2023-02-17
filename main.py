import json
import requests
from lxml import etree
from datetime import datetime

# Télécharger la page Web
url = "https://www.orientation.ch/dyn/show/2930?lang=fr&Idx=0&OrderBy=1&Order=0&PostBackOrder=0&postBack=true&CountResult=0&Total_Idx=0&CounterSearch=2&UrlAjaxWebSearch=%2FLenaWeb%2FAjaxWebSearch&getTotal=False&isBlankState=True&prof_=88613.1&fakelocalityremember=&LocName=&LocId=&Area=10&cty_=VD"
response = requests.get(url)

# Parser le contenu de la page téléchargée en utilisant etree
parser = etree.HTMLParser()
tree = etree.fromstring(response.content, parser)

# Extraire tous les éléments div contenant l'ancre "anchore"
resultbox = tree.xpath('//div[(@id="result-wrapper")]/div')

# Afficher les éléments extraits
del resultbox[::2]

for div in resultbox:
    company = div.findall('div')[0].text
    locality = div.findall('div')[2].text
    language = div.findall('div')[3].text
    year = div.findall('div')[4].text
    places = div.findall('div')[5].text.split()[0]
    lastUpdate = div.findall('div')[6].text
    origin = 'orientation.ch'
    originID = div.findall('div')[0].attrib["data-id"]
    date_obj = datetime.strptime(lastUpdate, '%d.%m.%y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    print(formatted_date)
    print(originID)
    apprenticeship = {
        'data':{
        'company': company,
        'locality': locality,
        'language': language,
        'year': year,
        'places': places,
        'lastUpdate': formatted_date,
        'origin': origin,
        'originID': int(originID)
        }
    }
    print(apprenticeship)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post("", headers=headers, data=json.dumps(apprenticeship))
    print(response.json())


