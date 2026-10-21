
def check_plausibilität(MESSUNG, min_wert, max_wert):
    return [wert for wert in MESSUNG if min_wert <= wert <= max_wert]

def del_duplicates(liste):
    return list(set(liste))

def print_messung(messung):
    print(f"Messung: {messung['CAN_Message']}, Wert: {messung['value']} {messung['unit']}, Zeitstempel: {messung['timestamp']}")    