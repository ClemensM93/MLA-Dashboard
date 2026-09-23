# Power BI – Anbindung Kommunikationskalender (SharePoint Online)

Diese Anleitung verbindet die SharePoint-Liste **"Kommunikationskalender neu"**
mit Power BI und richtet eine automatische (mehrmals tägliche) Aktualisierung ein.

- **Site-URL:** `https://porsche.sharepoint.com/sites/TeamsMEE150`
- **Liste:** `Kommunikationskalender neu`
- **Gateway nötig?** Nein (SharePoint Online ist eine Cloud-Quelle)

---

## 1. Verbindung herstellen (Power BI Desktop)

Zwei Wege – der Script-Weg ist am schnellsten:

### Variante A – Fertiges Script einfügen (empfohlen)
1. **Start → Neue Quelle → Leere Abfrage**
2. **Start → Erweiterter Editor**
3. Inhalt aus [Kommunikationskalender.pq](Kommunikationskalender.pq) komplett einfügen → **Fertig**
4. Erste Ausführung: Authentifizierung **Organisationskonto** → Porsche-Login
5. Spaltenliste im Script (`GewuenschteSpalten`) an die realen Spalten anpassen
6. **Start → Schließen & übernehmen**

### Variante B – Über die Oberfläche
1. **Daten abrufen → Mehr… → SharePoint Online-Liste**
2. Site-URL eingeben, **Implementierung 2.0** wählen
3. **Organisationskonto** → anmelden
4. Liste **Kommunikationskalender neu** anhaken → **Daten transformieren**
5. Nicht benötigte Spalten entfernen; Person-/Choice-Felder über das
   Erweitern-Symbol (⇄) auf `Value`/`Title` aufklappen; Datumstypen setzen

---

## 2. Measures hinzufügen
1. **Modellansicht** öffnen
2. Rechtsklick auf die Tabelle → **Neues Measure**
3. Blöcke aus [Measures.dax](Measures.dax) einzeln einfügen
   (Name = alles vor dem `=`, Formel = alles danach)

---

## 3. Visuals bauen (Vorschlag für einen Kalender)
- **Kalender-/Timeline-Visual** aus AppSource holen:
  *Visualisierungen → … → Weitere Visuals abrufen* → z. B. **"Calendar"** oder
  **"Timeline Storyteller"**
- KPI-Karten mit den Measures (Anzahl Kommunikationen, diesen Monat, nächste 30 Tage)
- Datenschnitt (Slicer) für **Format** und **Zeitraum**

---

## 4. Veröffentlichen & automatisch aktualisieren
1. **Start → Veröffentlichen** → Ziel-Arbeitsbereich wählen
2. Im **Power BI Service**: Arbeitsbereich → beim **semantischen Modell**
   auf **… → Einstellungen**
3. **Datenquellen-Anmeldeinformationen → Anmeldeinformationen bearbeiten**
   → OAuth2 / Organisationskonto → anmelden
4. **Geplante Aktualisierung** einschalten → z. B. 4 Uhrzeiten/Tag
   (mit Power BI Pro bis zu 8×/Tag möglich)

> Damit ist der Bericht mehrmals täglich aktuell – ohne Gateway.

---

## 5. Fertiger Bericht im Mockup-Stil (PBIP im Repo)

Dieses Repo enthält bereits ein fertig aufgebautes Modell + Bericht
(`KommunikationskalenderDashboard.pbip`) mit **zwei Seiten** im Stil von
[Dashboard_Mockup.html](Dashboard_Mockup.html):

- **Seite 1 „Kommunikationskalender"** – KPI-Karten (Beiträge gesamt,
  Σ Sichtbarkeit, Ø Resonanz, Ø Wirksamkeit), Beiträge pro Monat (gestapelt
  nach Format), Verteilung nach Format (Ring), Sichtbarkeit pro Monat,
  Wirkungskennzahlen je Format sowie Tabellen „Top-Beiträge" und „Kommende
  Beiträge".
- **Seite 2 „Befragungen (Check-in / Check-out)"** – KPI-Karten (Ø Relevanz
  Check-in, Ø Gefallen, Ø Umsetzungswahrscheinlichkeit, Ø Weiterempfehlung),
  Ø Relevanz je Impulsvortrag, Check-out-Kennzahlen, Antworten-Vergleich und
  Detailtabellen.

### Datenquellen im Modell
| Tabelle | SharePoint-Liste (Site `TeamsMEE150`) |
|---|---|
| `Kommunikationskalender alt` | Kommunikationskalender (Kalender-Liste) |
| `CheckIn` | `CheckIn Impuls Relevanz` |
| `CheckOut` | `CheckOut Impuls Relevanz` |

### Beziehungen (Datenmodell)
Die zentrale **`Kalender`**-Tabelle (Datumstabelle) verbindet den Kalender mit
den Bewertungen über das Datum – klassisches Stern-Schema:

| Von | Nach | Kardinalität | Richtung |
|---|---|---|---|
| `Kommunikationskalender alt[EventDatum]` | `Kalender[Datum]` | n : 1 | Kalender → Kalendereinträge |
| `CheckIn[Datum]` | `Kalender[Datum]` | n : 1 | Kalender → Check-in-Bewertungen |

Dadurch wirken Zeit-Datenschnitte (z. B. **Quartal**) gleichzeitig auf den
Kalender **und** auf die Check-in-Bewertungen. Das Check-in-Datum wird in Power
Query auf Mitternacht normalisiert, damit es exakt zu `Kalender[Datum]` passt.

> Die Check-out-Liste besitzt kein Datums-/Impulsvortrag-Feld und kann daher
> nicht über die Datumstabelle verknüpft werden. Sobald ein solches Feld
> ergänzt wird, lässt sich analog eine Beziehung `CheckOut[Datum] → Kalender[Datum]`
> anlegen.

### Spalten-Mapping der Befragungslisten
Die langen Fragetexte werden in Power Query auf kurze Modellnamen umbenannt
(siehe `…/tables/CheckIn.tmdl` und `CheckOut.tmdl`).

**Check-in:**
- „Auf welchen Impulsvortrag beziehen sich deine Angaben?" → `Impulsvortrag`
- „An welchem Datum findet der Impulsvortrag statt?" → `Datum`
- „Wie relevant schätzt du das Thema aktuell für dich ein?" → `Relevanz`

**Check-out:**
- „Wie wahrscheinlich ist es, dass du das Vorhaben … umsetzt?" → `Umsetzung`
- „Was ist der Grund, weshalb du dir nichts vornimmst?" → `Grund`
- „Wie hat dir der Impuls gefallen?" → `Gefallen`
- „…dass du den Impuls weiterempfiehlst?" → `Weiterempfehlung`

> **Wichtig:** In SharePoint kann der **interne** Spaltenname vom Anzeigenamen
> abweichen. Falls beim ersten Aktualisieren eine Spalte nicht gefunden wird,
> in `CheckIn.tmdl` / `CheckOut.tmdl` den Namen im Schritt `Umbenannt`
> (linke Seite) an den tatsächlichen Namen der Vorschau anpassen.
> Die Metrikspalten **Sichtbarkeit, Resonanz, Aktivierung, Wirksamkeit** müssen
> in der Kalender-Liste existieren – sonst bleiben die zugehörigen Karten leer.

### Hinweis zur Check-out-Seite
Die echte Check-out-Liste enthält **keine** erneute Relevanz-Frage und keinen
direkten Bezug (Impulsvortrag/Datum) zur Check-in-Liste. Der im Mockup gezeigte
„Relevanz-Uplift Check-in vs. Check-out je Thema" ist mit den realen Feldern
nicht 1:1 möglich. Die Seite bildet daher die **tatsächlich erhobenen**
Kennzahlen ab (Relevanz Check-in, Gefallen, Umsetzung, Weiterempfehlung).
Sobald die Check-out-Liste ein Impulsvortrag-/Datumsfeld erhält, lässt sich der
direkte Vorher/Nachher-Vergleich ergänzen.

---

## 6. Ausrollen ohne Desktop-App (nur Browser / Fabric)

Da nur die Cloud-Lösung genutzt wird, den fertigen PBIP-Ordner per
**Fabric Git-Integration** in den Arbeitsbereich bringen:

1. Repo (dieses Verzeichnis) in Azure DevOps / GitHub verfügbar machen.
2. Im **Power BI / Fabric Service**: Arbeitsbereich → **Workspace settings →
   Git integration** → Repo, Branch und Ordner `akademie-dashboard/powerbi`
   verbinden.
3. **Update all / Sync** ausführen → Semantikmodell und Bericht werden im
   Workspace erstellt.
4. Beim Semantikmodell **Datenquellen-Anmeldeinformationen** setzen
   (OAuth2 / Organisationskonto) und **geplante Aktualisierung** aktivieren
   (siehe Abschnitt 4).

### Optionales Design (Porsche-Look)
Für die volle Farbwelt des Mockups die Datei [PorscheTheme.json](PorscheTheme.json)
importieren: Bericht öffnen → **Ansicht → Designs → Design durchsuchen** →
`PorscheTheme.json` wählen. Grundlayout und Titel sind bereits im Bericht
hinterlegt.

---

## 7. Git-Repository & Workflow

Das Projekt liegt auf GitHub: **https://github.com/ClemensM93/MLA-Dashboard**
(Branch `main`, Repo-Root = Ordner `akademie-dashboard`, der `powerbi`-Ordner
enthält das PBIP-Projekt).

Änderungen ablegen und hochladen:

```powershell
cd "…/akademie-dashboard"
git add -A
git commit -m "Kurzbeschreibung der Änderung"
git push
```

Im **Power BI / Fabric Service** danach im Arbeitsbereich unter
**Git integration → Update all** die Änderungen übernehmen.


