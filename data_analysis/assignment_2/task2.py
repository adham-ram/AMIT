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
