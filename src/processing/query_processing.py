import pandas as pd
from src.data.excel_reader import read_excel_data
from src.filters.date_filter import filter_by_date
from src.filters.format_filter import filter_by_format

def process_query_data(excel_file, event_date, format_type):
    # Load data from the Excel file
    data = read_excel_data(excel_file)

    # Filter data by event date
    filtered_data = filter_by_date(data, event_date)

    # Further filter data by format type
    final_data = filter_by_format(filtered_data, format_type)

    return final_data

def get_event_data(excel_file, event_date):
    # Load data from the Excel file
    data = read_excel_data(excel_file)

    # Filter data by event date
    return filter_by_date(data, event_date)

def get_formats_data(excel_file):
    # Load data from the Excel file
    data = read_excel_data(excel_file)

    # Extract unique formats
    formats = data['Format'].unique()

    return formats.tolist()