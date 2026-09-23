from flask import Flask, render_template
from src.data.loader import load_data
from src.processing.query_processing import process_query_data
from src.processing.check_in_processing import process_check_in_data
from src.processing.check_out_processing import process_check_out_data
from src.filters.format_filter import filter_by_format
from src.filters.date_filter import filter_by_date

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from Excel
    data = load_data('data/kommunikationskalender.xlsx')
    
    # Process data
    query_data = process_query_data(data)
    check_in_data = process_check_in_data(data)
    check_out_data = process_check_out_data(data)
    
    # Render dashboard with processed data
    return render_template('dashboard.html', 
                           query_data=query_data, 
                           check_in_data=check_in_data, 
                           check_out_data=check_out_data)

if __name__ == '__main__':
    app.run(debug=True)