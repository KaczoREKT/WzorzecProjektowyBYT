# main.py
from Observer.Osoba import Osoba
from Subject.Subject import Subject
from Subject.RezerwacjaIndywidualna import RezerwacjaIndywidualna

if __name__ == "__main__":
    # Tworzenie subjectu
    rezerwacja = RezerwacjaIndywidualna("2025-01-01", "2025-01-01", "10:00", "12:00")

    # Tworzenie klientów
    osoba1 = Osoba(
        adres_e_mail="jan.kowalski@example.com",
        adres_zamieszkania="ul. Kwiatowa 15, 00-001 Warszawa",
        id=1,
        imie="Jan",
        nazwisko="Kowalski",
        numer_tel="123-456-789"
    )

    rezerwacja.dodajSubskrybenta(osoba1)
    # Dodawanie subskrybentów do subjectu


    # Tworzenie turnieju (brak turniejów na początku)
    turniej = RezerwacjaIndywidualna(
        data_rozpoczecia="2025-02-01",
        data_zakonczenia="2025-02-10",
        id=1,
        maksymalna_ilosc_uczestnikow=20,
        poziom_zaawansowania="",
        regulamin="Regulamin turnieju..."
    )

    # Symulacja: brak dostępnych turniejów
    print("Brak dostępnych turniejów na poziomie 1.")

    # Dodanie turnieju na poziomie 1
    subject.poziom_zaawansowania = "1"
    subject.powiadomSubskrybentow()

    turniej2 = RezerwacjaIndywidualna(
        data_rozpoczecia="2025-02-01",
        data_zakonczenia="2025-02-10",
        id=1,
        maksymalna_ilosc_uczestnikow=20,
        poziom_zaawansowania="2",
        regulamin="Regulamin turnieju..."
    )