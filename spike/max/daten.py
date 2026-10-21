MESSUNGEN = [
    {"akkustack": "Stack-1", "min-temp": 20.73, "max-temp": 54.31, "avg-temp": 35.61},
    {"akkustack": "Stack-2", "min-temp": 20.41, "max-temp": 54.28, "avg-temp": 35.92},
    {"akkustack": "Stack-3", "min-temp": 20.99, "max-temp": 54.18, "avg-temp": 35.43},
    {"akkustack": "Stack-4", "min-temp": 20.24, "max-temp": 54.57, "avg-temp": 35.14},
    {"akkustack": "Stack-5", "min-temp": 18.53, "max-temp": 54.24, "avg-temp": 34.45},
    {"akkustack": "Stack-6", "min-temp": 20.62, "max-temp": 54.31, "avg-temp": 35.56},
    {"akkustack": "Stack-7", "min-temp": 20.34, "max-temp": 62.11, "avg-temp": 39.97},
    {"akkustack": "Stack-8", "min-temp": 20.22, "max-temp": 54.45, "avg-temp": 35.18},

]
if __name__ == "__main__":
    for eintrag in MESSUNGEN:
        print(f"{eintrag['akkustack']:<12} min-Temp:{eintrag['min-temp']:5.1f}°C     max-Temp:{eintrag['max-temp']:5.1f}°C     avg-Temp:{eintrag['avg-temp']:5.1f}°C")