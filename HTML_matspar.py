mport re
import os
from pprint import pprint as pp

mat_hemsidor_output = ['frukt',
                       'farska-bar',
                       'fryst-frukt-bar',
                       'farska-gronsaker',
                       'potatis-rotfrukter-svamp',
                       'sallat-groddar',
                       'farska-kryddvaxter-orter',
                       'frysta-gronsaker',
                       'brod',
                       'knackebrod-skorpor',
                       'korvbrod-pitabrod-mm',
                       'fikabrod-tartor',
                       'kex-tilltugg',
                       'deg-bakmix',
                       'fryst-brod-desserter',
                       'kott',
                       'frysta-kottprodukter',
                       'kottbullar-biffar-nuggets',
                       'kyckling-fagel',
                       'korv',
                       'chark-palagg',
                       'blodpudding-sylta',
                       'fisk',
                       'kaviar-rom-saser',
                       'sill-anjovis-sardiner',
                       'skaldjur',
                       'fiskkonserver',
                       'mjolk',
                       'fil-yoghurt',
                       'smor-margarin',
                       'mellanmal-desserter',
                       'ost',
                       'gradde',
                       'graddfil-creme-fraiche',
                       'kvarg-cottage-cheese',
                       'havre-soja-risprodukter',
                       'agg',
                       'jast',
                       'asien',
                       'texmex',
                       'ovriga-varlden',
                       'kryddor-smaksattare',
                       'oljor-vinager-attika',
                       'pasta-ris-spannmal',
                       'baka',
                       'bonor-linser-artor',
                       'flingor-granola-musli',
                       'pulvermix',
                       'konserv-burk',
                       'sylt-mos-marmelad',
                       ] 

livsmedel_lista_lista = {}
for hemsida_text in mat_hemsidor_output:
    with open(os.getcwd() + f'\\Mat_app\\matspar_txt\\{hemsida_text}', "r", encoding="utf-8") as f:
        for rad in f.readlines():
            if "window.__PAGEDATA__" in rad:
                rad_split = rad.split(",")

                data = [re.sub(r"[^a-zA-Z0-9\s:åäöÅÄÖ]+", "", s) for s in rad_split]

                livsmedel_lista = {}
                livsmedel = [False, False, False]
                for string in data:
                    if "name:" in string:
                        index = string.find(":")
                        substring = string[index + 1 :]
                        if substring != '':
                            #words = substring.split()
                            #name = words[0]
                            livsmedel[0] = substring

                    elif "weightpretty:" in string:
                        index = string.find(":")
                        substring = string[index + 1 :]
                        if substring != '':
                            words = substring.split()
                            for word in words:
                                if word[0].isdigit():
                                    words = [word]
                            weight = words[0]
                            if "kg" in weight:
                                weight = int((re.findall(r"[0-9]+", weight))[0]) * 1000
                                livsmedel[1] = weight
                            else:
                                weight = int((re.findall(r"[0-9]+", weight))[0])
                                livsmedel[1] = weight

                    elif string.startswith("price:") and livsmedel[0]:
                        index = string.find(":")
                        substring = string[index + 1 :]
                        if substring != '':
                            words = substring.split()
                            for word in words:
                                if word[0].isdigit():
                                    words = [word]
                            price = words[0]
                            price = int(price) / 100
                            livsmedel[2] = price

                    if livsmedel[0] and livsmedel[1] and livsmedel[2]:
                        if livsmedel_lista == {}:
                            livsmedel_lista[livsmedel[0]] = {
                                "pris": livsmedel[2],
                                "vikt": livsmedel[1],
                            }
                            livsmedel = [False, False, False]
                        else:
                            livsmedel_lista_copy = list(livsmedel_lista.keys())
                            if livsmedel[0] not in livsmedel_lista_copy:
                                unique = True
                                for item in livsmedel_lista_copy:
                                    if livsmedel[0] in item:
                                        unique = False
                                for item in livsmedel_lista_copy:
                                    if item in livsmedel[0]:
                                        unique = False
                                if unique:
                                    livsmedel_lista[livsmedel[0]] = {
                                        "pris": livsmedel[2],
                                        "vikt": livsmedel[1],
                                    }
                                    livsmedel = [False, False, False]
                                livsmedel = [False, False, False]
                            livsmedel = [False, False, False]
    livsmedel_lista_lista = livsmedel_lista_lista | livsmedel_lista

# with open ('matspar_keys','w',encoding="utf-8") as f:
#     f.write(str(livsmedel_lista_lista.keys()))