def turki2farsi(tnumber):
    number = {
        "bir": 1,
        "iki": 2,
        "uoch": 3,
        "dord": 4,
        "besh": 5,
        "alteh": 6,
        "yedeh": 7,
        "sekiz": 8,
        "doghuz": 9,
        "on": 10
    }
    if tnumber in number:
        return number[tnumber]

tnumber = input("import the turki nember:")
fnumber = turki2farsi(tnumber)
if type(fnumber) == int:
    print("farsi number=", fnumber)
else:
    print(fnumber)





def turki_to_farsi(turkish_word):
    farsi_words = {
        "gharpuz": "هندوانه",
        "su": "آب"}
    if turkish_word in farsi_words:
        return farsi_words[turkish_word]
turki = input("import the turki word:")
farsi = turki_to_farsi(turki)
print(farsi)