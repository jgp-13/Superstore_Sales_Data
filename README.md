# **Superstore Sales Data Cleaning**

This repository contains a project for cleaning and transforming a messy **Superstore Sales Data** dataset. The dataset includes sales records from a retail business and contains issues such as missing values, duplicates, and inconsistent formatting, which were addressed to prepare the data for analysis and visualization.

## **Project Overview**

The objective of this project is to:
- Clean the raw sales data to make it ready for analysis.
- Remove duplicates and handle missing data.
- Standardize formats for dates and categorical variables.
- Prepare the dataset for effective data visualizations and business insights.

## **Dataset**

The dataset used in this project is the **Superstore Sales Data**, which contains the following columns:
- **order_id**: Unique identifier for each order.
- **order_date**: The date when the order was placed.
- **ship_date**: The date when the order was shipped.
- **ship_mode**: The shipping method used for the order.
- **customer_name**: Name of the customer who placed the order.
- **segment**: Customer segment (e.g., Consumer, Home Office, Corporate).
- **state**: State or region of the customer.
- **country**: The country where the customer is located.
- **market**: The market in which the order was placed (e.g., APAC, EMEA).
- **region**: Geographic region for the order.
- **category**: Product category (e.g., Office Supplies, Furniture).
- **sub_category**: The sub-category of the product.
- **product_name**: Name of the product.
- **sales**: Sales amount for the order.
- **quantity**: Quantity of items in the order.
- **discount**: Discount applied to the order.
- **profit**: Profit made from the order.
- **shipping_cost**: Cost of shipping the order.
- **order_priority**: Priority level of the order (e.g., Low, Medium, High).
- **year**: The year when the order was placed.

## **Data Cleaning Process**

The following steps were undertaken to clean the dataset:
1. **Duplicate Removal**: Identified and removed any duplicate records from the dataset.
2. **Handling Missing Values**: Imputed missing values using relevant strategies (e.g., mean imputation, deletion).
3. **Standardization**: Standardized column names and formats to ensure consistency.
4. **Date Formatting**: Converted `order_date` and `ship_date` to uniform date formats.
5. **Categorical Data**: Cleaned categorical data such as `order_priority`, `ship_mode`, and `segment` to ensure proper grouping.
6. **Outlier Detection**: Checked and handled outliers, especially in `sales`, `profit`, and `quantity` columns.
7. **Data Types**: Ensured proper data types (e.g., numerical, categorical, dates) for each column.

## **Technologies Used**

- **Python** (Pandas, NumPy)
- **Jupyter Notebook** (for documenting the analysis and cleaning process)
- **Git** (for version control)
- **CSV** (for data storage)

## **How to Run the Project**

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/jgp-13/superstore-sales-data-cleaning.git
   ```

2. Install the required libraries:
```
pip install pandas numpy
```
3. Open the Jupyter notebook file (e.g., `superstore_data_cleaning.ipynb`) and run the code cells to execute the data cleaning steps.

## **Results**

* A cleaned version of the dataset, ready for analysis and visualization.
* A detailed analysis of the cleaning process and decisions made at each stage.

## **Contributing**

Feel free to fork this repository and submit a pull request if you have suggestions or improvements. Ensure your code adheres to the project's coding standards and is well-documented.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





