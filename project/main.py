import pandas as pd
from config.config import file_path, drop_columns
from preprocessing import read_file, drop_unnecessary_columns, check_data_type

def pipeline():
    path = input("Please enter the path to the CSV file: ")
    if not path:
        path = file_path  # Use the default path from config if no input is provided
    df = read_file(path)
    drop_columns_by_user = input("Please enter the columns to drop (comma-separated), or press Enter to use default: ")
    if drop_columns_by_user:
        columns_to_drop = [col.strip() for col in drop_columns_by_user.split(',')]  
    else:
        columns_to_drop = drop_columns
    df = drop_unnecessary_columns(df, columns_to_drop)
    data_types = check_data_type(df)
    return df, data_types
results_df, data_types_df = pipeline()
print("Processed DataFrame:")
print(results_df)
print("\nData Types and Unique Values:")
print(data_types_df)