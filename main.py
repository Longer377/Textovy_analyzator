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

word_count = len(words)
titlecase_count = sum(1 for word in words if word[0].isupper())
uppercase_count = sum(1 for word in words if word.isupper())
lowercase_count = sum(1 for word in words if word.islower())
numeric_values = [float(word) for word in words if word.replace('.', '', 1).isdigit()]
numeric_count = len(numeric_values)
numeric_sum = int(sum(numeric_values))

length_distribution = {}
for word in words:
    cleaned_word = word.strip(",.!?;:\"'()[]{}")
    word_length = len(cleaned_word)
    if word_length not in length_distribution:
        length_distribution[word_length] = 0
    length_distribution[word_length] += 1

# Vypis analyzy

print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print("-" * 40)

print("LEN|  OCCURRENCES  |NR.")
print("-" * 40)

for word_length in sorted(length_distribution):
    stars = '*' * length_distribution[word_length]
    print(f"{word_length:3}|{stars:<19}|{length_distribution[word_length]}")






