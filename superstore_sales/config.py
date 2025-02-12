import os
import sys

# Get download source of the zip file
DATA_SOURCE_URL = 'https://www.kaggle.com/datasets/vivek468/superstore-dataset-final'

# Get absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Define key directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, '0-raw')
PROCESSED_DATA_DIR= os.path.join(DATA_DIR, '1-processed')
CLEANED_DATA_DIR= os.path.join(DATA_DIR, '2-cleaned')

NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')
FIGURES_DIR = os.path.join(NOTEBOOKS_DIR, 'figures')

PROJECT_DIR = os.path.join(BASE_DIR, 'project')

SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')

# Define key file paths
RAW_DATA_FILE = os.path.join(RAW_DATA_DIR, "SuperStoreOrders.csv")
CLEANED_DATA_FILE = os.path.join(CLEANED_DATA_DIR,'SuperStoreOrders_clean.csv')