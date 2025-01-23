from Observer import Observer


class Osoba(Observer):
    def __init__(self, adres_e_mail, adres_zamieszkania, id, imie, nazwisko, numer_tel):
        self.adres_e_mail = adres_e_mail
        self.adres_zamieszkania = adres_zamieszkania
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_tel = numer_tel

    def aktualizujInformacje(self, subject):
        print(f"Witaj {self.imie}! "
              f"\nZarejestrowaliśmy zmiany w twojej dotychczasowej rezerwacji. "
              f"\nOto jej nowe dane: "
              f"\nData rozpoczęcia: {subject.data_rozpoczecia}"
              f"\nData zakończenia: {subject.data_zakonczenia}"
              f"\nGodzina rozpoczęcia: {subject.godzina_rozpoczecia}"
              f"\nGodzina zakończenia {subject.godzina_zakonczenia}"
              f"\nPozdrawiamy!")

