from Subject.Subject import Subject

class Turniej(Subject):
    def __init__(self, data_rozpoczecia, data_zakonczenia, id, maksymalna_ilosc_uczestnikow, poziom_zaawansowania,
                 regulamin):
        super().__init__()
        self.data_rozpoczecia = data_rozpoczecia
        self.data_zakonczenia = data_zakonczenia
        self.id = id
        self.maksymalna_ilosc_uczestnikow = maksymalna_ilosc_uczestnikow
        self.poziom_zaawansowania = poziom_zaawansowania
        self.regulamin = regulamin
        print(f"Dodano nowy turniej na poziomie {self.poziom_zaawansowania}!")
        self.powiadomSubskrybentow()

    def powiadomSubskrybentow(self):
        print(f"Powiadamiam subskrybentów o turnieju na poziomie {self.poziom_zaawansowania}...")
        super().powiadomSubskrybentow()