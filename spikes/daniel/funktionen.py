def anzahl_messungen(messungen):
    return len(messungen)
"""wie viele messungen gibt es aktuell?"""


def mittelwert_druck(messungen):
    summe = 0
    for eintrag in messungen:
        summe += eintrag["luftdruck"]
    return summe / len(messungen)
"""was ist der durchschnittliche Luftdruck?"""


def messtellen_darstellen(messungen):
    messtellen = []
    for eintrag in messungen:
        messtellen.append(eintrag["station"])
    return messtellen
"""alle Messtellen anzeigen"""

