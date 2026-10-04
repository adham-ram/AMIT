import pandas as pd
import numpy as np
from config import DROP_COLS
def drop_columns(df, columns_to_drop=DROP_COLS):
    """
    Drops specified columns from the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns_to_drop (list): List of column names to drop.

    Returns:
    pd.DataFrame: DataFrame with specified columns dropped.
    """
    return df.drop(columns=columns_to_drop, errors='ignore')