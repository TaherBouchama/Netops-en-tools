import re
import yaml
import requests



url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"


ask = requests.get(url)
data = ask.text
resultaat = []


reg = r'(\d{2}+T)'
dag = re.search(reg, ask.text).group[1]

reg = r'/([0-9]{3}.\d{2}.\d{3}.\d{3})'
ip = re.search(reg, ask.text).group[1]


reg = r'[-.\/](0[1-9]|1[012])'
maand = re.search(reg, ask.text).group[1]

reg = r'(\d{4})'
jaar = re.search(reg, ask.text).group[0]

reg = r'/country\s*"(.*?)'
land = re.search(reg, ask.text).group[0]

reg = r'"ns3(.*?)"'
provider = re.search(reg, ask.text).group[0]


resultaat.__add__({'dag': dag, 'maand' : maand, 'jaar' : jaar, 'land' : land, 'provider' : provider})

if ask.status_code == 200:
    
    data= ask.json()
    yaml_rapport = yaml.dump({"create": resultaat})
    
    with open('resultaat.yaml', 'w') as yaml_file:
        yaml_file.write(yaml_rapport)
        
    print("de resultaat")

else:
    print(f"resultaat niet gevonden")