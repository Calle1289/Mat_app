from ingrediener import ingredienser, recept

print(list(recept.keys()))

recept_namn = ''
while recept_namn not in list(recept.keys()):
    recept_namn = input('Vilket recept: ')

total_vikt = 0
totalt_pris = 0

for i in recept[recept_namn]:  # Här räknar loopen ut vad kostnaden blir per portion
    total_vikt += i[1]
    totalt_pris += ingredienser[i[0]]['pris'] * (i[1] / ingredienser[i[0]]['vikt'])

portioner = input('En eller Fler portioner? ')

if portioner != 'En':
    portion_vikt = int(input('Vikt per portion: '))
else:
    portion_vikt = total_vikt

portion_pris = (portion_vikt / total_vikt) * totalt_pris

print(f'Totala priset blir {totalt_pris} och priset per portion blir {portion_pris}.')
