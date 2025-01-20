from datetime import datetime


# Interface Observer
class Observer:
    def update(self, message: str):
        raise NotImplementedError("Metoda update() musi być zaimplementowana.")


# Interface Subject
class Subject:
    def attach(self, observer: Observer):
        raise NotImplementedError("Metoda attach() musi być zaimplementowana.")

    def detach(self, observer: Observer):
        raise NotImplementedError("Metoda detach() musi być zaimplementowana.")

    def notify(self, message: str):
        raise NotImplementedError("Metoda notify() musi być zaimplementowana.")


# ConcreteSubject
class Lekcja(Subject):
    def __init__(self):
        self._observers = []
        self.data = None
        self.data_zakonczenia = None
        self.godzina_rozpoczecia = None
        self.godzina_zakonczenia = None
        self.id = None

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

    def ustaw_nowy_termin(self, data, godzina_rozpoczecia, godzina_zakonczenia):
        self.data = data
        self.godzina_rozpoczecia = godzina_rozpoczecia
        self.godzina_zakonczenia = godzina_zakonczenia
        self.notify(f"Nowy termin lekcji: {data} od {godzina_rozpoczecia} do {godzina_zakonczenia}.")


# ConcreteObserver
class Klient(Observer):
    def __init__(self, poziom_zaawansowania: str, imie: str):
        self.poziom_zaawansowania = poziom_zaawansowania
        self.imie = imie

    def update(self, message: str):
        print(f"Powiadomienie dla {self.imie}: {message}")


# Przykład użycia
if __name__ == "__main__":
    lekcja = Lekcja()

    klient1 = Klient("średniozaawansowany", "Jan")
    klient2 = Klient("początkujący", "Anna")

    # Rejestracja klientów
    lekcja.attach(klient1)
    lekcja.attach(klient2)

    # Dodanie nowego terminu
    lekcja.ustaw_nowy_termin(datetime(2025, 2, 15), "10:00", "11:00")

    # Usunięcie jednego klienta
    lekcja.detach(klient1)

    # Dodanie kolejnego terminu
    lekcja.ustaw_nowy_termin(datetime(2025, 2, 16), "12:00", "13:00")
