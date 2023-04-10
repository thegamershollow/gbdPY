import requests
from bs4 import BeautifulSoup

# the base url for vimms lair's vault
baseUrl = 'https://www.vimm.net/vault/'

# grabs data from the urls provided by the loop
systems = ['GB','GBC','GBA','NES','SNES','N64','Wii','GameCube','WiiWare','DS']
for sysItems in systems:
    sysName = sysItems
    print('\n**'+sysItems+'**\n')
    letters = ['/A','/B','/C','/D','/E','/F','/G','/H','/I','/J','/K','/L','/M','/N','/O','/P','/Q','/R','/S','/T','/U','/V','/W','/X','/Y','/Z']
    for items in letters:
        #HTML parser
        grab = requests.get(baseUrl+sysName+items)
        soup = BeautifulSoup(grab.text, 'html.parser')
        ids = soup.find_all('tr')
        print(baseUrl+sysName+items)
        with open(sysName+'-title-list.txt', 'a') as f:
            f.write(sysName)
            f.write('\n'+items+'\n')
            for line in ids:
                f.write('%s\n' % line)