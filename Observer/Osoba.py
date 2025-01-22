from Observer.Observer import Observer


class Osoba(Observer):
    def __init__(self, adres_e_mail, adres_zamieszkania, id, imie, nazwisko, numer_tel):
        self.adres_e_mail = adres_e_mail
        self.adres_zamieszkania = adres_zamieszkania
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_tel = numer_tel

