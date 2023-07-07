def farsi2turki(number):
    turki_number = {1:"Bir",2:"iki",3:"uoch",4:"Dord",5:"Besh",6:"Alteh",7:"Yedeh",8:"Sekiz",9:"Doghuz",10:"Oun"}
    if number in turki_number:
        return turki_number[number]
    else:
        return "this isnt defind"

number = int(input("give number:"))
turki_number = farsi2turki(number)
print(turki_number)