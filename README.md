# Fibonacci-Modulor-Rechner 📐🧮

Dieses Python-Skript generiert eine Fibonacci-Reihe innerhalb eines benutzerdefinierten Bereichs und berechnet Modulor-Module basierend auf den Dimensionen einer Fläche, die in Millimetern angegeben werden. Es ist ein nützliches Tool für Architekten und Designer, die das Modulor-System von Le Corbusier in ihren Projekten anwenden möchten.

## Voraussetzungen 📋

Um dieses Skript auszuführen, benötigen Sie Python auf Ihrem Computer. Python kann von der offiziellen Website [python.org](https://www.python.org/downloads/) heruntergeladen und installiert werden. Folgen Sie den Anweisungen für Ihr Betriebssystem.

## Ausführung des Skripts 🚀

Öffnen Sie Ihre Kommandozeile oder Ihr Terminal und navigieren Sie zu dem Verzeichnis, in dem das Skript gespeichert ist. Führen Sie das Skript mit dem folgenden Befehl aus:

```bash
python fibonacci_modulor_calculator.py
```

## Benutzereingaben 🔠

Nach dem Start des Skripts werden Sie aufgefordert, verschiedene Eingaben zu machen:

1. **Anfangswert der Fibonacci-Reihe**: Geben Sie den kleinsten Wert ein, ab dem die Fibonacci-Reihe generiert werden soll (z.B. 3). Die Reihe wird immer mit 0 und 1 beginnen, aber nur Werte, die größer oder gleich diesem Anfangswert sind, werden in der Ausgabe berücksichtigt.

2. **Endwert der Fibonacci-Reihe**: Geben Sie den maximalen Wert ein, bis zu dem die Fibonacci-Reihe generiert werden soll (z.B. 55). Die Reihe wird anhalten, sobald ein Wert größer als dieser Endwert erreicht wird.

3. **Gesamtbreite in mm**: Geben Sie die Breite der Fläche ein, für die die Modulor-Module berechnet werden sollen (z.B. 257 mm).

4. **Gesamthöhe in mm**: Geben Sie die Höhe der Fläche ein, für die die Modulor-Module berechnet werden sollen (z.B. 378 mm).

Das Skript wird dann die Fibonacci-Reihe ausgeben, die Modulor-Module berechnen und sicherstellen, dass die Summe der Module den angegebenen Dimensionen entspricht.

## Beispiel 🌟

```plaintext
Geben Sie den Anfangswert der Fibonacci-Reihe ein (z.B. 3): 3
Geben Sie den Endwert der Fibonacci-Reihe ein (z.B. 55): 55
Geben Sie die Gesamtbreite in mm ein (z.B. 257): 257
Geben Sie die Gesamthöhe in mm ein (z.B. 378): 378

Generierte Fibonacci-Reihe von 3 bis 55: [3, 5, 8, 13, 21, 34, 55]
Summe der Fibonacci-Reihe: 139

Modulor-Module (Einzelwerte und Summen):
3 Einheiten: Horizontal = 5.554 mm, Vertikal = 8.165 mm
...
Summe der horizontalen Modulor-Module: 257.0 mm (Soll: 257 mm)
Summe der vertikalen Modulor-Module: 378.0 mm (Soll: 378 mm)
```

## Was ist eine Fibonacci-Reihe? 🔢

Die Fibonacci-Reihe ist eine Folge von Zahlen, bei der jede Zahl die Summe der beiden vorhergehenden Zahlen ist. Die einfachste Form der Reihe beginnt mit 0 und 1. Hier ist ein kurzes Beispiel:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

## Lizenz 📄

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Weitere Details finden Sie in der `LICENSE`-Datei.

Viel Spaß beim Nutzen des Fibonacci-Modulor-Rechners!
```
Kopieren Sie diesen Inhalt in eine `README.md`-Datei in Ihrem GitHub-Repository, um eine ansprechende und informative Beschreibung für Ihr Projekt zu haben.
