from Subject.Subject import Subject

class RezerwacjaIndywidualna(Subject):
    def __init__(self, data_rozpoczecia, data_zakonczenia, godzina_rozpoczecia, godzina_zakonczenia):
        super().__init__()
        self.data_rozpoczecia = data_rozpoczecia
        self.data_zakonczenia = data_zakonczenia
        self.godzina_rozpoczecia = godzina_rozpoczecia
        self.godzina_zakonczenia = godzina_zakonczenia

    def dodajSubskrybenta(self, observer):
        if observer not in self.subskrybenci:
            self.subskrybenci.append(observer)

    def usunSubskrybenta(self, observer):
        if observer in self.subskrybenci:
            self.subskrybenci.remove(observer)

    def powiadomSubskrybentow(self):
        for subskrybent in self.subskrybenci:
            subskrybent.aktualizujInformacje(self.data_rozpoczecia, self.data_zakonczenia, self.godzina_rozpoczecia, self.godzina_zakonczenia)

    # Funkcja sprawdza czy podany atrybut istnieje, a następnie zmienia jego wartość na tą podaną w funkcji
    def zmienDaneRezerwacji(self, **kwargs):
        zmienione_dane = {}
        for attr, value in kwargs.items():
            if value is not None and hasattr(self, attr):
                setattr(self, attr, value)
                zmienione_dane[attr] = value
        if zmienione_dane:
            self.powiadomSubskrybentow(zmienione_dane)

