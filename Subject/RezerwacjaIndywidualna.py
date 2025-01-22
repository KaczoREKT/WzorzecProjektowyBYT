from Subject.Subject import Subject

class RezerwacjaIndywidualna(Subject):
    def __init__(self, data_rozpoczecia, data_zakonczenia, godzina_rozpoczecia, godzina_zakonczenia):
        super().__init__()
        self.data_rozpoczecia = data_rozpoczecia
        self.data_zakonczenia = data_zakonczenia
        self.godzina_rozpoczecia = godzina_rozpoczecia
        self.godzina_zakonczenia = godzina_zakonczenia


    def powiadomSubskrybentow(self):
        super().powiadomSubskrybentow()

    # Funkcja sprawdza czy podany atrybut istnieje, a następnie zmienia jego wartość na tą podaną w funkcji
    def zmienDaneRezerwacji(self, **kwargs):
        for attr, value in kwargs.items():
            if value is not None and hasattr(self, attr):
                setattr(self, attr, value)
