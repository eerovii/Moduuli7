nimi = input('Anna nimesi: ')
nimet = set()

while nimi != '':
    for i in nimet:
        if nimi == i: print('Aiemmin syöttämäsi nimi: ')
    else: print('Uusi nimi: ')
    nimet.add(nimi)
    nimi = input('Anna nimesi: ')
for i in nimet:
    print(i)