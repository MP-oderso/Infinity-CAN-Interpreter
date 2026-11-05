def mittelwert(daten, feld):
    """Mittelwert eines Zahlenfeldes über alle Datensätze."""
    werte = [eintrag[feld] for eintrag in daten]
    return sum(werte) / len(werte)
def filternmin(daten, feld, minimum):
    """Alle Datensätze, deren Feld mindestens 'minimum' beträgt."""
    return [eintrag for eintrag in daten if eintrag[feld] >= minimum]
def filternmax(daten, feld, maximum):
    """Alle Datensätze, deren Feld mindestens 'maximum' beträgt."""
    return [eintrag for eintrag in daten if eintrag[feld] <= maximum]
def maximum(daten, feld):
    """Der Datensatz mit dem größten Wert im Feld."""
    return max(daten, key=lambda eintrag: eintrag[feld])
def minimum(daten, feld):
    """Der Datensatz mit dem kleinsten Wert im Feld."""
    return min(daten, key=lambda eintrag: eintrag[feld])