import pandas as pd

def read_excel(file_path):
    """
    Reads the Excel file and returns a DataFrame.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=None)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

def extract_event_data(df):
    """
    Extracts event data from the DataFrame.
    Assumes the relevant data is in a specific sheet named 'Query'.
    """
    if 'Query' in df:
        event_data = df['Query']
        return event_data
    else:
        print("Query sheet not found in the Excel file.")
        return None

def extract_check_in_data(df):
    """
    Extracts check-in survey data from the DataFrame.
    Assumes the relevant data is in a specific sheet named 'Check In'.
    """
    if 'Check In' in df:
        check_in_data = df['Check In']
        return check_in_data
    else:
        print("Check In sheet not found in the Excel file.")
        return None

def extract_check_out_data(df):
    """
    Extracts check-out survey data from the DataFrame.
    Assumes the relevant data is in a specific sheet named 'Check Out'.
    """
    if 'Check Out' in df:
        check_out_data = df['Check Out']
        return check_out_data
    else:
        print("Check Out sheet not found in the Excel file.")
        return None

def main():
    file_path = '../data/kommunikationskalender.xlsx'
    df = read_excel(file_path)
    
    if df is not None:
        event_data = extract_event_data(df)
        check_in_data = extract_check_in_data(df)
        check_out_data = extract_check_out_data(df)
        
        # Further processing can be done here
        print(event_data.head())
        print(check_in_data.head())
        print(check_out_data.head())

if __name__ == "__main__":
    main()