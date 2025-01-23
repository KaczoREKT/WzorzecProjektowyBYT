# main.py
from Osoba import Osoba
from RezerwacjaIndywidualna import RezerwacjaIndywidualna

if __name__ == "__main__":
    # Tworzenie klientów
    osoba1 = Osoba(
        adres_e_mail="stanisław.wyszomirski@interia.pl",
        adres_zamieszkania="ul. Krasnalowa 21, 00-007 Warka",
        id=1,
        imie="Stanisław",
        nazwisko="Wyszomirski",
        numer_tel="987654321"
    )
    # Tworzenie subjectu
    rezerwacja = RezerwacjaIndywidualna("2025-01-01", "2025-01-01", "10:00", "12:00")
    rezerwacja.dodajSubskrybenta(osoba1)

    rezerwacja.zmienDaneRezerwacji(godzina_rozpoczecia='8:00')
