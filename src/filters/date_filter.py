def filter_events_by_date(events, start_date, end_date):
    """
    Filters a list of events based on a date range.

    Parameters:
    events (list): A list of event dictionaries, each containing a 'date' key.
    start_date (datetime): The start date for filtering.
    end_date (datetime): The end date for filtering.

    Returns:
    list: A list of events that fall within the specified date range.
    """
    filtered_events = [
        event for event in events
        if start_date <= event['date'] <= end_date
    ]
    return filtered_events

def get_unique_event_dates(events):
    """
    Extracts unique event dates from a list of events.

    Parameters:
    events (list): A list of event dictionaries, each containing a 'date' key.

    Returns:
    set: A set of unique event dates.
    """
    unique_dates = {event['date'] for event in events}
    return unique_dates