from Observer import Observer


class Osoba(Observer):
    def __init__(self, adres_e_mail, adres_zamieszkania, id, imie, nazwisko, numer_tel):
        self.adres_e_mail = adres_e_mail
        self.adres_zamieszkania = adres_zamieszkania
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_tel = numer_tel

    def aktualizujInformacje(self, dane):
        print(f"Witaj {self.imie}! "
              f"\nZarejestrowaliśmy zmiany w twojej dotychczasowej rezerwacji. "
              f"\nOto jej nowe dane: "
              f"\nData rozpoczęcia: {dane.data_rozpoczecia}"
              f"\nData zakończenia: {dane.data_zakonczenia}"
              f"\nGodzina rozpoczęcia: {dane.godzina_rozpoczecia}"
              f"\nGodzina zakończenia {dane.godzina_zakonczenia}"
              f"\nPozdrawiamy!")

