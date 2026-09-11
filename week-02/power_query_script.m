// ==========================================================
// ZYROO DATA ANALYST INTERNSHIP — WEEK 2
// Power BI - Power Query M Transformation Script
// Project: Ride Analytics & Revenue Intelligence Platform
// ==========================================================

let
    // OPTION A: Local File Path
    // Source = Csv.Document(File.Contents("C:\Users\Sakthibalan\.gemini\antigravity\scratch\zyro-data-analyst-internship\week-02\rides_data_cleaned.csv"), [Delimiter=",", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]),

    // OPTION B: Cloud Live Web Connection (GitHub / Google Sheets Web CSV)
    Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/evilswordboy-bot/zyro-data-analyst-internship/main/week-02/rides_data_cleaned.csv"), [Delimiter=",", Columns=8, Encoding=65001, QuoteStyle=QuoteStyle.None]),

    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),

    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"Ride ID", type text}, 
        {"Date", type date}, 
        {"Pickup Location", type text}, 
        {"Drop-off Location", type text}, 
        {"Fare", Int64.Type}, 
        {"Payment Method", type text}, 
        {"Ride Status", type text}, 
        {"Rating", type number}
    }),

    // Data Cleaning Step: Remove negative or invalid fares
    #"Filtered Negative Fares" = Table.SelectRows(#"Changed Type", each [Fare] >= 0),

    // Data Cleaning Step: Remove duplicate Ride IDs
    #"Removed Duplicates" = Table.Distinct(#"Filtered Negative Fares", {"Ride ID"})
in
    #"Removed Duplicates"
