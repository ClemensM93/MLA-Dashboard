from flask import render_template
from src.data.loader import load_data
from src.processing.query_processing import process_query_data
from src.processing.check_in_processing import process_check_in_data
from src.processing.check_out_processing import process_check_out_data
from src.filters.format_filter import filter_by_format
from src.filters.date_filter import filter_by_date

def generate_kpi_cards(selected_format=None, start_date=None, end_date=None):
    # Load data from the Excel file
    data = load_data('data/kommunikationskalender.xlsx')
    
    # Process query data
    query_data = process_query_data(data)
    
    # Filter data by selected format if provided
    if selected_format:
        query_data = filter_by_format(query_data, selected_format)
    
    # Filter data by date range if provided
    if start_date and end_date:
        query_data = filter_by_date(query_data, start_date, end_date)
    
    # Process check-in and check-out data
    check_in_data = process_check_in_data(data)
    check_out_data = process_check_out_data(data)
    
    # Generate KPI metrics
    total_events = len(query_data)
    average_check_in = sum(check_in_data) / len(check_in_data) if check_in_data else 0
    average_check_out = sum(check_out_data) / len(check_out_data) if check_out_data else 0
    
    # Prepare KPI card data
    kpi_cards = {
        'total_events': total_events,
        'average_check_in': average_check_in,
        'average_check_out': average_check_out
    }
    
    return render_template('kpi_cards.html', kpi_cards=kpi_cards)