import pandas as pd
def read_file(path):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a parsing error while reading the file.")
        return None
    
def drop_unnecessary_columns(df, columns_to_drop):
    """
    Drops specified columns from a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame from which to drop columns.
    columns_to_drop (list): A list of column names to drop.

    Returns:
    pd.DataFrame: The DataFrame with the specified columns dropped.
    """
    return df.drop(columns=columns_to_drop)

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