from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

class EventTimeline:
    def __init__(self, data):
        self.data = data

    def filter_by_format(self, format_name):
        return self.data[self.data['Format'] == format_name]

    def plot_timeline(self, format_name):
        filtered_data = self.filter_by_format(format_name)
        if filtered_data.empty:
            print(f"No events found for format: {format_name}")
            return

        dates = pd.to_datetime(filtered_data['Event Date'])
        events = filtered_data['Event Name']

        plt.figure(figsize=(10, 6))
        plt.plot(dates, range(len(dates)), marker='o', linestyle='-', color='b')
        plt.yticks(range(len(events)), events)
        plt.title(f'Event Timeline for {format_name}')
        plt.xlabel('Date')
        plt.ylabel('Events')
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def generate_timeline(self):
        formats = self.data['Format'].unique()
        for format_name in formats:
            self.plot_timeline(format_name)