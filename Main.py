from App.ClientApp import ClientApp
from App.TrainerApp import TrainerApp
from Observer.Klient import Klient
from Subject.Lekcja import Lekcja

if __name__ == "__main__":
    lekcja = Lekcja()

    # Trainer GUI
    trainer_app = TrainerApp(lekcja)

    # Client 1
    klient1 = Klient("Klient 1")
    lekcja.attach(klient1)
    client_app1 = ClientApp(klient1)

    # Run GUIs
    import threading

    threading.Thread(target=trainer_app.run).start()
    threading.Thread(target=client_app1.run).start()
