# main.py
from Observer.Osoba import Osoba
from Subject.RezerwacjaIndywidualna import RezerwacjaIndywidualna

if __name__ == "__main__":
    # Tworzenie klientów
    osoba1 = Osoba(
        adres_e_mail="jan.kowalski@example.com",
        adres_zamieszkania="ul. Kwiatowa 15, 00-001 Warszawa",
        id=1,
        imie="Jan",
        nazwisko="Kowalski",
        numer_tel="123-456-789"
    )
    # Tworzenie subjectu
    rezerwacja = RezerwacjaIndywidualna("2025-01-01", "2025-01-01", "10:00", "12:00")
    rezerwacja.dodajSubskrybenta(osoba1)

    rezerwacja.zmienDaneRezerwacji(godzina_rozpoczecia ='13:00')


