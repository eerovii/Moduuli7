Vuodenajat=('kesä', 'syksy', 'talvi', 'kevät')

kuukausi=int(input('Anna kuukausi numerona (1-12): '))

if kuukausi in (1, 2, 12):
    print(Vuodenajat[2])
elif kuukausi in (3, 4, 5):
    print(Vuodenajat[3])
elif kuukausi in (6, 7, 8):
    print(Vuodenajat[0])
elif kuukausi in (9, 10, 11):
    print(Vuodenajat[1])
else: print('Antamasi numero ei vastaa mitään kuukautta.')