import pandas as pd


def check_unique_values(dataframe: pd.DataFrame) -> dict:
    """
    Automatically identifies and checks the unique values in each
    categorical column (object or category dtype) of the DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe to check.

    Returns:
    dict: A dictionary with categorical column names as keys and a 
          list of all the unique values as values.
    """
    # Automatically identify categorical columns by checking their data type
    categorical_cols = dataframe.select_dtypes(include=['object', 'category']).columns

    # Initialize the dictionary to store results
    unique_values_dict = {}

    if len(categorical_cols) == 0:
        print("No columns of 'object' or 'category' dtype were found.")
        return unique_values_dict

    print(f"Found {len(categorical_cols)} categorical column(s) to check.")

    for col in categorical_cols:
        # Get the unique values
        unique_vals = dataframe[col].unique().tolist()
        unique_values_dict[col] = unique_vals

    return unique_values_dict

