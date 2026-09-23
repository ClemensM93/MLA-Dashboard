# Akademie Dashboard

This project is designed to create a dashboard for the Akademie, utilizing data extracted from a SharePoint site. The dashboard provides insights into various formats offered by the Akademie, along with evaluations from check-in and check-out surveys.

## Project Structure

```
akademie-dashboard
├── data
│   └── kommunikationskalender.xlsx  # Contains data extracted from SharePoint
├── src
│   ├── app.py                        # Main entry point of the application
│   ├── data
│   │   ├── loader.py                 # Functions to load data from Excel
│   │   └── excel_reader.py           # Functions to read data from Excel
│   ├── processing
│   │   ├── query_processing.py        # Processes event dates from the query tab
│   │   ├── check_in_processing.py     # Processes check-in survey data
│   │   └── check_out_processing.py    # Processes check-out survey data
│   ├── filters
│   │   ├── format_filter.py           # Functions to filter data by format
│   │   └── date_filter.py             # Functions to filter data by date
│   ├── components
│   │   ├── kpi_cards.py               # Generates KPI cards for the dashboard
│   │   ├── format_overview.py         # Provides an overview of different formats
│   │   ├── event_timeline.py          # Visualizes the timeline of events
│   │   └── survey_charts.py           # Generates charts for survey results
│   └── config
│       └── settings.py                # Configuration settings for the application
├── tests
│   ├── test_loader.py                 # Unit tests for data loading functionality
│   ├── test_query_processing.py        # Unit tests for query processing functions
│   └── test_filters.py                # Unit tests for filtering functions
├── requirements.txt                   # Lists dependencies required for the project
└── README.md                          # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd akademie-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage Guidelines

- The dashboard will display various formats of the Akademie along with their evaluations.
- Users can filter events by date and format to view specific data.
- Check-in and check-out survey results are visualized through charts for better insights.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.