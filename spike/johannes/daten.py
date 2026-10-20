#daten test

messungen = [{"data": "ort1", "x1": 10, "x2": 20, "x3": 30},
             {"data": "ort2", "x1": 15, "x2": 25, "x3": 35},
             {"data": "ort3", "x1": 20, "x2": 30, "x3": 40}]

if __name__ == "__main__":
    for messung in messungen:
        print(f"Messung an {messung['data']}: x1={messung['x1']}, x2={messung['x2']}, x3={messung['x3']}")