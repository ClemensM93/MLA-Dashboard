// ============================================================================
// Power Query (M) – SharePoint-Liste "Kommunikationskalender neu"
// ----------------------------------------------------------------------------
// Verwendung:
//   1. Power BI Desktop -> Start -> Neue Quelle -> Leere Abfrage
//   2. Start -> Erweiterter Editor
//   3. Diesen gesamten Code einfuegen und "Fertig" klicken
//   4. Beim ersten Ausfuehren: Anmeldung mit "Organisationskonto" (Porsche-Login)
//
// Hinweis: Passe die Liste "Behaltene Spalten" (Schritt SpaltenAuswahl) an die
// tatsaechlichen Spalten deiner Liste an. Fuehre die Abfrage einmal aus und
// entferne/ergaenze Spaltennamen entsprechend der Vorschau.
// ============================================================================
let
    // --- Konfiguration -------------------------------------------------------
    SiteUrl   = "https://porsche.sharepoint.com/sites/TeamsMEE150",
    ListName  = "Kommunikationskalender neu",

    // --- Verbindung zur SharePoint Online-Liste (Implementierung 2.0) --------
    Quelle    = SharePoint.Tables(
                    SiteUrl,
                    [ApiVersion = 15, Implementation = "2.0", ViewMode = "All"]
                ),

    // Liste anhand des Anzeigenamens auswaehlen
    Liste     = Quelle{[Title = ListName]}[Items],

    // --- Nur relevante Spalten behalten -------------------------------------
    // TIPP: Nach dem ersten Ausfuehren pruefst du in der Vorschau die realen
    // Spaltennamen und passt diese Liste an. Unbekannte Spalten werden ignoriert.
    GewuenschteSpalten = {
        "Title",            // Titel des Kommunikations-Eintrags
        "Format",           // Kommunikationsformat (Kanal)
        "Startdatum",       // Startdatum
        "Enddatum",         // Enddatum
        "Status",           // Status
        "Verantwortlich",   // Person-Feld
        "Zielgruppe",       // Zielgruppe
        "Beschreibung",     // Beschreibung / Details
        "Created",          // Erstellt am
        "Modified"          // Geaendert am
    },
    VorhandeneSpalten = List.Intersect({ Table.ColumnNames(Liste), GewuenschteSpalten }),
    SpaltenAuswahl    = Table.SelectColumns(Liste, VorhandeneSpalten, MissingField.Ignore),

    // --- Person-Feld "Verantwortlich" auf Anzeigenamen aufklappen -----------
    // Person-/Lookup-Felder kommen als Record. Falls die Spalte existiert,
    // wird der Anzeigename (Title) extrahiert; sonst uebersprungen.
    VerantwortlichAufklappen =
        if Table.HasColumns(SpaltenAuswahl, "Verantwortlich") then
            Table.TransformColumns(
                SpaltenAuswahl,
                {{"Verantwortlich", each if _ = null then null
                                         else if Value.Is(_, type record) then Record.FieldOrDefault(_, "Title", null)
                                         else _, type text}}
            )
        else SpaltenAuswahl,

    // --- Datentypen setzen (nur fuer vorhandene Spalten) --------------------
    TypDefinitionen = {
        {"Startdatum", type datetime},
        {"Enddatum",   type datetime},
        {"Created",    type datetime},
        {"Modified",   type datetime},
        {"Title",      type text},
        {"Format",     type text},
        {"Status",     type text},
        {"Zielgruppe", type text},
        {"Beschreibung", type text}
    },
    GueltigeTypen = List.Select(TypDefinitionen, each Table.HasColumns(VerantwortlichAufklappen, {_{0}})),
    TypenGesetzt  = Table.TransformColumnTypes(VerantwortlichAufklappen, GueltigeTypen),

    // --- Hilfsspalten fuer Zeit-Analysen ------------------------------------
    MitJahrMonat =
        if Table.HasColumns(TypenGesetzt, "Startdatum") then
            Table.AddColumn(
                Table.AddColumn(TypenGesetzt, "Jahr", each try Date.Year([Startdatum]) otherwise null, Int64.Type),
                "MonatNr", each try Date.Month([Startdatum]) otherwise null, Int64.Type
            )
        else TypenGesetzt
in
    MitJahrMonat
