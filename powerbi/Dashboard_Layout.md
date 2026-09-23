# Dashboard-Bauplan – Kommunikationskalender (Power BI)

Fertiges Layout, das du in Power BI Desktop nachbaust. Nur der Kommunikations-
kalender wird verwendet (die 3 Impuls-Listen sind noch leer).

**Reihenfolge:**
1. [Kalendertabelle.dax](Kalendertabelle.dax) einfügen + Beziehung ziehen
2. [Measures.dax](Measures.dax) als Measures anlegen
3. Seiten & Visuals wie unten aufbauen

---

## 0. Modell vorbereiten
- Tabelle heisst bei dir `Kommunikationskalender alt` (Namen so belassen).
  Reale Spalten: `Event Date` (Start), `End Time` (Ende), `Format`, `Title`,
  `Recurrence`, `ID`.
- **Kalender**-Tabelle anlegen (Script) und Beziehung:
  `Kalender[Datum]` → `Kommunikationskalender alt[Event Date]` (1:n)
- Kalender als **Datumstabelle markieren** (Spalte `Datum`)

---

## Farb-/Designleitfaden (Porsche-nah)
| Element | Farbe |
|---|---|
| Primär / Akzent | `#0072CE` (Blau) |
| Sekundär | `#1A1A1A` (Nahezu Schwarz) |
| Erfolg / abgeschlossen | `#2E7D32` |
| Warnung / in Arbeit | `#F9A825` |
| Kritisch / offen | `#C62828` |
| Hintergrund Karten | `#FFFFFF` mit dezentem Schatten |
| Seitenhintergrund | `#F4F5F7` |

Schriftart: **Porsche Next** (falls installiert), sonst **Segoe UI**.

---

## Seite 1 – „Überblick"

**Kopfzeile (ganze Breite)**
- Textfeld/Card mit Measure **[Titel dynamisch]** als Überschrift
- Rechts: Datenschnitt **Zeitraum** (Kalender[JahrMonat] als „Zwischen"-Slider)

**KPI-Karten-Reihe (4 Karten nebeneinander)**
1. **[Anzahl Kommunikationen]** – „Gesamt"
2. **[Kommunikationen diesen Monat]** – „Diesen Monat"
   - Trend: **[Veraenderung ggue Vormonat %]** als Detail
3. **[Kommunikationen naechste 30 Tage]** – „Nächste 30 Tage"
4. **[Anzahl Formate]** – „Formate"

**Mittelblock (2 Visuals nebeneinander)**
- Links: **Säulendiagramm** „Kommunikationen pro Monat"
  - X-Achse: `Kalender[Monat]` (nach `MonatNr` sortiert)
  - Y-Achse: **[Anzahl Kommunikationen]**
  - Legende optional: `Format`
- Rechts: **Ringdiagramm** „Verteilung nach Format"
  - Legende: `Format`, Werte: **[Anzahl Kommunikationen]**

**Fußblock (ganze Breite)**
- **Tabelle** „Kommende Kommunikationen"
  - Spalten: `Event Date`, `Title`, `Format`, `End Time`
  - Filter (Visual-Ebene): `Event Date` ist **an oder nach heute**
  - Sortierung: `Event Date` aufsteigend
  - Bedingte Formatierung der Spalte `Format` über Measure **[Farbe Format]**

---

## Seite 2 – „Kalenderansicht"

- **Custom Visual** installieren: *Visualisierungen → … → Weitere Visuals abrufen*
  → **„Calendar"** (Autor: MAQ Software) oder **„Beyondsoft Calendar"**
- Feldzuordnung:
  - **Datum:** `Kommunikationskalender alt[Event Date]`
  - **Wert/Legende:** `Format` (für Farbcodierung)
- Darunter Datenschnitte: `Format`, Zeitraum (`Kalender[Datum]`)

**Alternative ohne Custom Visual:** Matrix
- Zeilen: `Kalender[KW]`, Spalten: `Kalender[Wochentag]`
- Werte: **[Anzahl Kommunikationen]**, Zellen bedingt einfärben

---

## Seite 3 – „Formate & Details" (Drill-Through)

- **Balkendiagramm** „Top Formate": Achse `Format`, Wert **[Anzahl Kommunikationen]**
- **Matrix** „Format × Monat":
  - Zeilen `Format`, Spalten `Kalender[Monat]`, Werte **[Anzahl Kommunikationen]**
- **Drill-Through** einrichten: Feld `Format` in den Drill-Through-Bereich ziehen,
  damit man von Seite 1 per Rechtsklick auf ein Format hierher springt.

---

## Interaktions-/Slicer-Empfehlung (alle Seiten)
Als **Synchronisierte Datenschnitte** (Ansicht → Datenschnitte synchronisieren):
- `Format` (Dropdown)

- `Kalender[JahrMonat]` oder `Kalender[Datum]` (Zeitraum)

---

## Feinschliff
- **Ansicht → Seiten an Größe anpassen:** 16:9
- Karten: einheitliche Höhe, dezenter Schatten, abgerundete Ecken
- Titel jeder Visual sprechend benennen (deutsch)
- **QuickInfo (Tooltip)-Seite** optional für Detailanzeige beim Hover
- Nach Fertigstellung: **Veröffentlichen** und geplante Aktualisierung prüfen
  (siehe [README.md](README.md))

---

### Checkliste
- [ ] Kalendertabelle erstellt + Beziehung (`Kalender[Datum]` → `Event Date`) + als Datumstabelle markiert
- [ ] Sortierspalten gesetzt (Monat, JahrMonat, Wochentag)
- [ ] Alle Measures angelegt
- [ ] Seite 1 Überblick gebaut
- [ ] Seite 2 Kalenderansicht gebaut
- [ ] Seite 3 Formate/Drill-Through gebaut
- [ ] Slicer synchronisiert
- [ ] Veröffentlicht + Aktualisierung geplant
