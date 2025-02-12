# Data Visualization - SuperStore Sales

## Overview
This notebook explores the cleaned SuperStore Sales dataset using **Seaborn** and **Matplotlib** to uncover key insights. The visualizations help analyze profit distribution, sales trends, and the impact of discounts on profitability.

## Key Visualizations & Insights

### 1️. Profit Distribution
- The histogram shows a **leptokurtic** distribution, meaning profit values are clustered around the mean with extreme highs and lows.
- A **boxplot confirms** the presence of significant outliers, indicating high variability in profitability.

### 2. Sales, Quantity, Discount, and Profit Distributions
- Boxplots reveal different distribution patterns for these key business metrics.
- Outliers in discount and profit suggest cases where excessive discounts might be hurting revenue.

### 3. Correlation Analysis
- Discounts have a **weak correlation (-0.028) with Sales** but a **stronger negative correlation (-0.219) with Profit**.
- This suggests that increasing discounts **reduces profitability** rather than driving more sales.

### 4. Discount vs. Profit Relationship
- A **scatter plot** confirms the negative impact of high discounts on profit.
- It is shown a **Discount** of more than **20%** would be highly probable to generate losses.
- Negative profits (marked in red) increase as discount levels rise.

### 5. Sales Performance Across Discount Levels
- A **bar chart** highlights how sales volume changes with different discount levels.
- Some discounts increase sales, but profitability remains a concern.

## Technologies Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **Parquet format file  was chosen over the other files with different formats**

## How to Use This Notebook
1. Ensure you have the cleaned dataset (`SuperStoreOrders_clean.parquet`) in the `data/2-cleaned/` folder.
2. Run the notebook to generate visualizations and explore key business insights.

## Next Steps
- Build an **interactive Tableau or Power BI dashboard** to further enhance insights.
- Conduct **time-series analysis** to detect sales trends over time.
- Explore **clustering methods** to segment customers based on purchasing behavior.

