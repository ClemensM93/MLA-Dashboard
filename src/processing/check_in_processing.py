import pandas as pd

def process_check_in_data(excel_file, format_filter=None):
    # Load the data from the Excel file
    df = pd.read_excel(excel_file, sheet_name='Check In')

    # Filter by format if specified
    if format_filter:
        df = df[df['Format'] == format_filter]

    # Process the check-in data
    processed_data = {
        'total_responses': df['Response'].count(),
        'average_rating': df['Rating'].mean(),
        'responses_by_date': df.groupby('Date')['Response'].count().to_dict(),
        'average_rating_by_date': df.groupby('Date')['Rating'].mean().to_dict()
    }

    return processed_data

def main():
    # Example usage
    excel_file = '../data/kommunikationskalender.xlsx'
    format_filter = 'Workshop'  # Example format filter
    check_in_results = process_check_in_data(excel_file, format_filter)
    print(check_in_results)

if __name__ == "__main__":
    main()