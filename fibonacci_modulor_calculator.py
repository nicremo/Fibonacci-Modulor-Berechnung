# Funktion, um die Fibonacci-Reihe zu generieren
def generiere_fibonacci_reihe(anfang, ende):
    reihe = [0, 1]  # Startwerte der Fibonacci-Reihe
    while reihe[-1] < ende:
        next_value = reihe[-1] + reihe[-2]
        reihe.append(next_value)
    return [x for x in reihe if x >= anfang and x <= ende]

# Funktion, um die Modulor-Werte zu berechnen
def berechne_modulor(breite_mm, hoehe_mm, fibonacci_reihe):
    summe_fibonacci = sum(fibonacci_reihe)
    einheit_horizontal_mm = breite_mm / summe_fibonacci
    einheit_vertikal_mm = hoehe_mm / summe_fibonacci
    
    module_horizontal = [round(einheit * einheit_horizontal_mm, 3) for einheit in fibonacci_reihe]
    module_vertikal = [round(einheit * einheit_vertikal_mm, 3) for einheit in fibonacci_reihe]
    
    return module_horizontal, module_vertikal, summe_fibonacci

# Werte abfragen
anfang_der_reihe = int(input("Geben Sie den Anfangswert der Fibonacci-Reihe ein (z.B. 3): "))
ende_der_reihe = int(input("Geben Sie den Endwert der Fibonacci-Reihe ein (z.B. 55): "))
breite = float(input("Geben Sie die Gesamtbreite in mm ein (z.B. 257): "))
hoehe = float(input("Geben Sie die Gesamthöhe in mm ein (z.B. 378): "))

# Fibonacci-Reihe generieren
fibonacci_reihe = generiere_fibonacci_reihe(anfang_der_reihe, ende_der_reihe)
print(f"\nGenerierte Fibonacci-Reihe von {anfang_der_reihe} bis {ende_der_reihe}: {fibonacci_reihe}")

# Modulor-Module berechnen
module_hor, module_ver, summe_fibonacci = berechne_modulor(breite, hoehe, fibonacci_reihe)
print(f"Summe der Fibonacci-Reihe: {summe_fibonacci}")

# Ergebnisse ausgeben und Summe überprüfen
print("\nModulor-Module (Einzelwerte und Summen):")
summe_horizontal = 0
summe_vertikal = 0
for i, einheit in enumerate(fibonacci_reihe):
    summe_horizontal += module_hor[i]
    summe_vertikal += module_ver[i]
    print(f"{einheit} Einheiten: Horizontal = {module_hor[i]} mm, Vertikal = {module_ver[i]} mm")

# Überprüfen, ob die Summen korrekt sind
print(f"\nSumme der horizontalen Modulor-Module: {summe_horizontal} mm (Soll: {breite} mm)")
print(f"Summe der vertikalen Modulor-Module: {summe_vertikal} mm (Soll: {hoehe} mm)")

# Überprüfen, ob die berechneten Summen den eingegebenen Breiten und Höhen entsprechen
assert round(summe_horizontal, 3) == round(breite, 3), "Die Summe der horizontalen Module entspricht nicht der eingegebenen Breite."
assert round(summe_vertikal, 3) == round(hoehe, 3), "Die Summe der vertikalen Module entspricht nicht der eingegebenen Höhe."