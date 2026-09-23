from flask import Blueprint, render_template
from src.data.loader import load_data
from src.processing.query_processing import process_query_data
from src.processing.check_in_processing import process_check_in_data
from src.processing.check_out_processing import process_check_out_data
from src.filters.format_filter import filter_by_format
from src.filters.date_filter import filter_by_date

format_overview_bp = Blueprint('format_overview', __name__)

@format_overview_bp.route('/format_overview')
def format_overview():
    # Load data from the Excel file
    data = load_data('data/kommunikationskalender.xlsx')
    
    # Process the query data to get event dates
    query_data = process_query_data(data)
    
    # Process check-in and check-out data
    check_in_data = process_check_in_data(data)
    check_out_data = process_check_out_data(data)
    
    # Filter data by format and date
    filtered_formats = filter_by_format(query_data)
    filtered_dates = filter_by_date(query_data)

    return render_template('format_overview.html', 
                           formats=filtered_formats, 
                           check_in=check_in_data, 
                           check_out=check_out_data,
                           dates=filtered_dates)