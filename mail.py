import time

slowa = {
    'LOL': 'odpowiedź na coś zabawnego',
    'CRINGE': 'coś dziwnego lub wstydliwego',
    'ROFL': 'odpowiedź na żart',
    'SHEESH': 'lekka dezaprobata',
    'CREEPY': 'straszny, złowieszczy',
    'AGGRO': 'stać się agresywnym/zły',
    'SKIBIDI': '1. co jest dziwne jak skibidi toilet. 2. ala zabawne',
    'REL': 'określenie czegoś prawdziwego lub prawdziwego też wobec siebie',
    'ŚPIULKOLOT': 'stare określenie łóżka używane w 21w.',
    'LIDLONKA': 'osoba która lubi Lidla i Biedronkę',
    'BRUH': 'jako westchnienie wyrażające frustrację i niezadowolenie, czasem zdumienie, odpowiednik o, bracie',
    'XD': 'śmieszne',
    'Xd': 'ha ha... takie sobie',
    'xd': 'EEeeeee... słabe',
    'xD': 'trochę to mnie rozbawiło'
}

while True:  # Pętla nieskończona
    slowo = input('Podaj słowo z CAPS LOCK (oprócz rodzajów XD): ')

    if slowo in slowa:
        print(slowa[slowo])
    else:
        print('Nie znam tego słowa. Może spróbuj wpisać je inaczej?')
        print('https://www.youtube.com/watch?v=xm3YgoEiEDc')

    for i in range(4, 0, -1):
        print(i)
        time.sleep(0.5)

    # Po odliczaniu program pyta o nowe słowo
    slowo = input('Podaj kolejne słowo z CAPS LOCK (oprócz rodzajów XD): ')
