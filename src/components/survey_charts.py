import pandas as pd
import matplotlib.pyplot as plt

def load_survey_data(file_path):
    # Load the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Load check-in and check-out data
    check_in_data = pd.read_excel(xls, sheet_name='CheckIn')
    check_out_data = pd.read_excel(xls, sheet_name='CheckOut')
    
    return check_in_data, check_out_data

def filter_data_by_format(data, format_name):
    return data[data['Format'] == format_name]

def plot_survey_charts(check_in_data, check_out_data, format_name):
    # Filter data for the specific format
    filtered_check_in = filter_data_by_format(check_in_data, format_name)
    filtered_check_out = filter_data_by_format(check_out_data, format_name)

    # Create a figure with subplots
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Check-in survey results
    axs[0].bar(filtered_check_in['Date'], filtered_check_in['Score'], color='blue')
    axs[0].set_title(f'Check-In Survey Results for {format_name}')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Score')

    # Check-out survey results
    axs[1].bar(filtered_check_out['Date'], filtered_check_out['Score'], color='green')
    axs[1].set_title(f'Check-Out Survey Results for {format_name}')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Score')

    plt.tight_layout()
    plt.show()

def generate_survey_charts(file_path, format_name):
    check_in_data, check_out_data = load_survey_data(file_path)
    plot_survey_charts(check_in_data, check_out_data, format_name)