from daten import MESSUNGEN
from funktionen import anzahl_messungen, mittelwert_druck, messtellen_darstellen

if __name__ == "__main__":
    print(f"Anzahl Messungen: {anzahl_messungen(MESSUNGEN)}")
    print(f"{mittelwert_druck(MESSUNGEN): .3f} hPa")
    print(messtellen_darstellen(MESSUNGEN))
