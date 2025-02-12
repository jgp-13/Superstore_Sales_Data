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

- **Row ID**: A unique identifier for each row.
- **Order ID**: A unique identifier for each order.
- **Order Date**: The date on which the order was placed.
- **Ship Date**: The date on which the order was shipped.
- **Ship Mode**: The shipping method used for the order.
- **Customer ID**: A unique identifier for each customer.
- **Customer Name**: The name of the customer who placed the order.
- **Segment**: The customer segment (Consumer, Corporate and Home Office).
- **Country**: The country where the customer is located.
- **City**: The city where the customer is located.
- **State**: The state of the customer.
- **Postal Code**: The postal code of the customer's location.
- **Region**: The geographic region where the order was placed.
- **Product ID**: A unique identifier for each product.
- **Category**: The category of the product.
- **Sub-Category**: The sub-category of the product.
- **Product Name**: The name of the product.
- **Sales**: The total sales amount for the order.
- **Quantity**: The quantity of items in the order.
- **Discount**: The discount applied to the order.
- **Profit**: The profit made from the order.

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
For file storage:
   * **CSV** 
   * **json**
   * **Parquet**
   * **Pickle**

  
## **Results**

* A cleaned version of the dataset, ready for analysis and visualization.
* 3 Extra columns:
- **Product ID dup**: A boolean mask indicating duplicated product IDs.
- **Product ID updated**: The product identifier after being identified as updated.
- **Shipping Duration**: The time taken for the order to be shipped, typically measured from the order date to the ship date.

* A detailed analysis of the cleaning process and decisions made at each stage.

## **Contributing**

Feel free to fork this repository and submit a pull request if you have suggestions or improvements. Ensure your code adheres to the project's coding standards and is well-documented.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





