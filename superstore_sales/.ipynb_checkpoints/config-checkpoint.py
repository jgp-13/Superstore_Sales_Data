import os
import sys

# Get download source of the zip file
DATA_SOURCE_URL = 'https_//www.kaggle.com/datasets/aditisaxena20/superstore-sales-dataset/SuperStore_Orders.scv.zip'

# Get absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.abspath(os.getcwd()))

#Define key directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, '0-raw')
PROCESSED_DATA_DIR= os.path.join(DATA_DIR, '1-processed')
CLEANED_DATA_DIR= os.path.join(DATA_DIR, '2-cleaned')

NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks')

PROJECT_DIR = os.path.join(BASE_DIR, 'project')

SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')