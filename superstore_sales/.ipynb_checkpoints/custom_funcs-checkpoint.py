# custom_funcs.py

def clean_data(df):
    """Clean the data by handling missing values and removing duplicates."""
    df = df.dropna()  # Drop rows with missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df