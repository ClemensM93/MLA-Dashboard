import pandas as pd

def process_check_out_data(file_path, format_filter=None):
    # Load the data from the Excel file
    data = pd.read_excel(file_path, sheet_name='Check Out')

    # Filter by format if specified
    if format_filter:
        data = data[data['Format'] == format_filter]

    # Process the data as needed for visualization
    processed_data = {
        'total_responses': data['Response'].count(),
        'average_rating': data['Rating'].mean(),
        'feedback_comments': data['Comments'].dropna().tolist()
    }

    return processed_data

def main():
    file_path = '../data/kommunikationskalender.xlsx'
    format_filter = None  # Set to a specific format if needed

    check_out_summary = process_check_out_data(file_path, format_filter)
    print(check_out_summary)

if __name__ == "__main__":
    main()