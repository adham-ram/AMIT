import pandas as pd
def check_data_type(df):
    """
    Checks the data types of each column in a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to check.

    Returns:
    pd.Series: A Series containing the data types of each column.
    """
    column_data_types = df.dtypes
    columns_names = df.columns
    number_of_unique_values = df.nunique()
    return pd.DataFrame({
        'Column Name': columns_names,
        'Data Type': column_data_types,
        'Unique Values': number_of_unique_values
    })