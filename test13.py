def turki_to_farsi(turkish_word):
    farsi_words = {
        "gharpuz": "هندوانه",
        "su": "آب"}
    if turkish_word in farsi_words:
        return farsi_words[turkish_word]
turki = input("turki word?")
farsi = turki_to_farsi(turki)
print(farsi)