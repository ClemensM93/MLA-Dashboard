def filter_by_format(data, format_type):
    """
    Filters the provided data based on the specified format type.

    Parameters:
    data (list of dict): The data to filter, where each dict represents a record.
    format_type (str): The format type to filter by.

    Returns:
    list of dict: The filtered data containing only records that match the specified format type.
    """
    return [record for record in data if record.get('format') == format_type]

def get_unique_formats(data):
    """
    Retrieves a list of unique format types from the provided data.

    Parameters:
    data (list of dict): The data to analyze.

    Returns:
    set: A set of unique format types found in the data.
    """
    return set(record.get('format') for record in data)