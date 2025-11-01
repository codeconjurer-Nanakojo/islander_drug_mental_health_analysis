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


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_numerical_distributions(dataframe: pd.DataFrame, file_name: str = 'numerical_distributions.png'):
    """
    Automatically identifies all numerical columns in the DataFrame and plots
    their distributions using seaborn.histplot, saving the result to a file.

    Parameters:
    dataframe (pd.DataFrame): The input dataframe to check.
    file_name (str): The name of the file to save the figure (default: 'numerical_distributions.png').
    """

    # 1. Identify all numerical columns
    numerical_cols = dataframe.select_dtypes(include=np.number).columns

    if len(numerical_cols) == 0:
        print("No numerical columns found in the DataFrame.")
        return

    n_features = len(numerical_cols)

    # 2. Determine optimal subplot grid size
    # Aim for a layout that is visually appealing, like 3 or 4 columns wide
    n_cols = 3
    n_rows = int(np.ceil(n_features / n_cols))

    # 3. Create the figure and subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))

    # Flatten the axes array if it's 2D for easy iteration
    axes = axes.flatten() if n_rows > 1 else np.array([axes]).flatten()

    # 4. Iterate and plot
    for i, col in enumerate(numerical_cols):
        # Use seaborn's histplot for distribution
        sns.histplot(dataframe[col], kde=True, ax=axes[i], bins=20, edgecolor='k')
        axes[i].set_title(f'Distribution of {col}', fontsize=14)
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Count')

    # 5. Hide any unused subplots
    for j in range(n_features, len(axes)):
        fig.delaxes(axes[j])

    # 6. Adjust layout to prevent overlap and save
    plt.tight_layout(pad=3.0)
    plt.savefig(file_name)
    plt.close(fig)  # Close the figure to free up memory

    print(f"Successfully generated and saved histogram plots for {n_features} numerical features to '{file_name}'.")