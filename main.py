TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {"bob": "123",
        "ann": "pass123", 
        "mike": "password123", 
        "liz": "pass123"}

# Prihlaseni uzivatele
username = input("Zadej uživatelské jméno:")
user_password = input("Zadej své heslo:")

if username in users and users[username] == user_password:
    print(f"Ahoj {username.title()}, jdeme analyzovat :] ")
elif username in users and users[username] != user_password:
    print(f"Ahoj {username.title()}, znám tě ale heslo je špatně. Ukončuji program.")
    exit()
else:
    print(f"{username.title()}, nejsi registrovany. Ukončuji program.")
    exit()

# Volba textu 
selected_text = input("Zadej číslo textu, který chceš analyzovat:")

if not selected_text.isdigit():
    print("Zadána neplatná hodnota, ukončuji program.")
    exit()
elif (int(selected_text)) > len(TEXTS) or (int(selected_text)) <= 0:
    print("Zadána hodnota mimo rozsah, ukončuji program.")
    exit()
else:
    print(f"Zvolen text č.{selected_text}")

# Analyza

selected_text = int(selected_text) - 1

words = TEXTS[selected_text].split()

pocet_slov = len(words)
zacina_velkym = sum(1 for w in words if w[0].isupper())
velkymi = sum(1 for w in words if w.isupper())
malymi = sum(1 for w in words if w.islower())
cisla = [float(w) for w in words if w.replace('.', '', 1).isdigit()]
pocet_cisel = len(cisla)
soucet_cisel = int(sum(cisla))

delky = {}
for w in words:
    w = w.strip(",.!?;:\"'()[]{}")
    delka = len(w)
    if delka not in delky:
        delky[delka] = 0
    delky[delka] += 1

# Vypis analyzy

print("-" * 40)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {zacina_velkym} titlecase words.")
print(f"There are {velkymi} uppercase words.")
print(f"There are {malymi} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {soucet_cisel}")
print("-" * 40)

print("LEN|  OCCURRENCES  |NR.")
print("-" * 40)

for d in sorted(delky):
    hvezdy = '*' * delky[d]
    print(f"{d:3}|{hvezdy:<19}|{delky[d]}")






