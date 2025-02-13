import pandas as pd  
import numpy as np 
from IPython.display import display  


def dup_flag(df, id_col, value_col):
    """
    Identifies duplicate IDs based on their associated values.

    Args:
        df (pd.DataFrame): The input DataFrame.
        id_col (str): Column containing IDs.
        value_col (str): Column to check for uniqueness within each ID.

    Returns:
        dup_flags (pd.Series): Boolean Series indicating which rows have duplicate IDs.
        unique_combinations (pd.DataFrame): DataFrame with unique (id_col, value_col) combinations.
    """
    unique_combinations = df[[id_col, value_col]].drop_duplicates().copy()
    dup_prod = df.groupby(id_col)[value_col].nunique()
    dup_ids = dup_prod[dup_prod > 1].index.to_list()
    dup_flags = df[id_col].isin(dup_ids)
    return dup_flags, unique_combinations

def update_id(df, id_col, value_col):
    """
    Updates duplicate IDs by appending a numerical suffix.

    Args:
        df (pd.DataFrame): The input DataFrame.
        id_col (str): Column containing IDs.
        value_col (str): Column to check for uniqueness within each ID.

    Returns:
        pd.DataFrame: DataFrame with updated IDs and duplication flags.
    """
    flags = dup_flag(df, id_col, value_col)
    df[id_col + ' dup'] = flags[0]  # Boolean flag for duplicate IDs
    suffixes = flags[1]  # DataFrame with unique ID-value combinations
    suffixes[id_col + ' suffix'] = suffixes.groupby(id_col).cumcount() + 1  # Assign incremental suffix
    new_col = id_col + ' updated'
    suffixes[new_col] = suffixes[id_col].astype(str) + "_" + suffixes[id_col + ' suffix'].astype(str).str.zfill(2)
    
    # Drop redundant columns if they exist
    df = df.drop(columns=[col for col in [id_col + ' suffix', new_col] if col in df.columns], axis=1)
    
    # Merge updated suffixes with original DataFrame
    df_new = df.merge(suffixes, on=[id_col, value_col], how='left')
    
    # Keep original ID where no duplicates exist
    df_new[new_col] = np.where(df_new[id_col + " dup"], df_new[new_col], df_new[id_col])

    return df_new

def compare_info(df1, df2, df1_name="Raw Data", df2_name="Cleaned Data"):
    '''
    Compares the basic structure of two DataFrames side by side, showing data types
    and non-null counts for each column.
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame (raw data).
    df2 (pd.DataFrame): The second DataFrame (cleaned data).
    df1_name (str): Label for the first DataFrame.
    df2_name (str): Label for the second DataFrame.
    '''
    from IPython.display import display
    import pandas as pd
    
    info_raw = pd.DataFrame(df1.dtypes, columns=[df1_name])
    info_raw['Non-Null Count'] = df1.notnull().sum()
    
    info_clean = pd.DataFrame(df2.dtypes, columns=[df2_name])
    info_clean['Non-Null Count'] = df2.notnull().sum()
    
    info_comparison = pd.concat([info_raw, info_clean], axis=1)
    display(info_comparison)

# Function to compare memory usage
def compare_memory_usage(df1, df2):
    '''
    Compares the memory usage of two DataFrames and prints the results in megabytes (MB).
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame (raw data).
    df2 (pd.DataFrame): The second DataFrame (cleaned data).
    '''
    mem_raw = df1.memory_usage(deep=True).sum() / 1e6
    mem_clean = df2.memory_usage(deep=True).sum() / 1e6
    print(f"\nMemory Usage (MB):\nRaw Data: {mem_raw:.2f} MB\nCleaned Data: {mem_clean:.2f} MB")

# Function to check missing values
def compare_missing_values(df1, df2):
    '''
    Compares missing values between two DataFrames and returns a DataFrame
    showing the count of missing values in each dataset.
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame (raw data).
    df2 (pd.DataFrame): The second DataFrame (cleaned data).
    
    Returns:
    pd.DataFrame: A DataFrame containing the missing value count for each dataset.
    '''
    import pandas as pd
    
    missing_raw = df1.isnull().sum()
    missing_clean = df2.isnull().sum()
    missing_comparison = pd.DataFrame({
        'Raw Data': missing_raw,
        'Cleaned Data': missing_clean
    })
    return missing_comparison[missing_comparison.sum(axis=1) > 0]


# Function to compare column data types
def compare_dtypes(df1, df2):
    '''
    Compares the data types of columns between two DataFrames and returns
    columns where data types differ.
    
    Parameters:
    df1 (pd.DataFrame): The first DataFrame (raw data).
    df2 (pd.DataFrame): The second DataFrame (cleaned data).
    
    Returns:
    pd.DataFrame: A DataFrame showing columns with differing data types.
    '''
    dtypes_raw = df1.dtypes.astype(str)
    dtypes_clean = df2.dtypes.astype(str)
    dtype_comparison = pd.DataFrame({
        'Raw Data': dtypes_raw,
        'Cleaned Data': dtypes_clean
    })
    return dtype_comparison[dtype_comparison["Raw Data"] != dtype_comparison["Cleaned Data"]]
