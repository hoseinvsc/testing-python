def farsi2turki(number):
    turki_number = {"bir":1,"iki":2,"uoch":3,"Dord":4,"Besh":5,"Alteh":6,"Yedeh":7,"Sekiz":8,"Doghuz":9,"Oun":10}
    if number in turki_number:
        return turki_number[number]
    else:
        return "this isnt defind"

number = int(input("give number:"))
turki_number = farsi2turki(number)
print(turki_number)




def turki2farsi(turki_number):
    farsinumber = {
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
    if turki_number in farsinumber:
        return farsinumber[turki_number]
    return "errore"

turki_number = input("import the turki nember:")
farsi_number = turki2farsi(turki_number)
if type(farsi_number) == int:
    print("farsi number=", farsi_number)
else:
    print(farsi_number)
