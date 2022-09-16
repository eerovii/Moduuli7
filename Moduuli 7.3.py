lentoK={}
doExit=True

while doExit:
    komento=input('Kirjoita "T" tallentaaksesi uusi lentokenttä \n Kirjoita "E" etsiäksesi lentokentää \n Lopeta jättämällä kenttä tyhjäksi\nKomento: ').upper()
    if komento=='T':
        lentoK[input('Anna lentokentän ICAO-koodi: ')]=input('Anna lentokentän nimi: ')
    elif komento=='E':
        nimi = input('Anna etsittävän lentokentän ICAO-koodi: ')
        if nimi in lentoK: print(lentoK[nimi])
        else: print('Kyseistä lentokenttää ei löydy.')
    else: doExit=False