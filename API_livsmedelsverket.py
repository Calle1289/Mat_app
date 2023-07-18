import requests
import xml.etree.ElementTree as ET
from pprint import pprint as pp

# API livsmedelsverket

response = requests.get(
    "http://www7.slv.se/apilivsmedel/LivsmedelService.svc/Livsmedel/Naringsvarde/20230701"
)

content = response.content.decode("utf-8")

root = ET.fromstring(content)

tree = ET.ElementTree(root)

livsmedel_lista = {}

for livsmedel in root.findall("./LivsmedelsLista/Livsmedel"):
    for namn in livsmedel.findall("./Namn"):
        livsmedel_lista[namn.text] = {}

    for ViktGram in livsmedel.findall("./ViktGram"):
        livsmedel_lista[namn.text][ViktGram.tag] = ViktGram.text

    for naringsvarden in livsmedel.findall("./Naringsvarden"):
        livsmedel_lista[namn.text][naringsvarden.tag] = {}

    for naringsvarde in livsmedel.findall("./Naringsvarden/Naringsvarde"):
        for naringsvarde_namn in naringsvarde.findall("./Namn"):
            livsmedel_lista[namn.text][naringsvarden.tag][naringsvarde_namn.text] = {}
        for naringsvarde_varde in naringsvarde.findall("./Varde"):
            varde_dot = naringsvarde_varde.text.replace(",", ".")
            if "\xa0" in varde_dot:
                varde_dot = varde_dot.replace("\xa0", "")
            livsmedel_lista[namn.text][naringsvarden.tag][naringsvarde_namn.text][
                naringsvarde_varde.tag
            ] = varde_dot
        for naringsvarde_enhet in naringsvarde.findall("./Enhet"):
            livsmedel_lista[namn.text][naringsvarden.tag][naringsvarde_namn.text][
                naringsvarde_enhet.tag
            ] = naringsvarde_enhet.text
# with open('livsmedelsverket.txt', 'w', encoding='utf-8') as f:
#     f.write(str(livsmedel_lista))