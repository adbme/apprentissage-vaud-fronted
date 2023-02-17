import requests
from bs4 import BeautifulSoup

# Télécharger la page Web
url = "https://www.orientation.ch/dyn/show/2930?lang=fr&Idx=0&OrderBy=1&Order=0&PostBackOrder=0&postBack=true&CountResult=0&Total_Idx=0&CounterSearch=2&UrlAjaxWebSearch=%2FLenaWeb%2FAjaxWebSearch&getTotal=False&isBlankState=True&prof_=88613.1&fakelocalityremember=&LocName=&LocId=&Area=10&cty_=VD"
response = requests.get(url)

# Créer l'objet BeautifulSoup à partir du contenu de la page téléchargée
soup = BeautifulSoup(response.content, "html.parser")

# Extraire tous les éléments div contenant une ID qui commence par "anchore"
elements = soup.find_all("div", {"id": lambda x: x and x.startswith("anchor")})


