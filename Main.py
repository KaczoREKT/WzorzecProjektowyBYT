# main.py
from Observer.Klient import Klient
from Subject.Subject import Subject
from Subject.Turniej import Turniej

if __name__ == "__main__":
    # Tworzenie subjectu
    subject = Subject()

    # Tworzenie klientów
    klient1 = Klient(poziom_zaawansowania="1")
    klient2 = Klient(poziom_zaawansowania="2")

    # Dodawanie subskrybentów do subjectu
    subject.dodajSubskrybenta(klient1)
    subject.dodajSubskrybenta(klient2)

    # Tworzenie turnieju (brak turniejów na początku)
    turniej = Turniej(
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

    turniej2 = Turniej(
        data_rozpoczecia="2025-02-01",
        data_zakonczenia="2025-02-10",
        id=1,
        maksymalna_ilosc_uczestnikow=20,
        poziom_zaawansowania="2",
        regulamin="Regulamin turnieju..."
    )