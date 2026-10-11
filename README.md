# Business Sales Performance Analytics

## Project Overview

Business Sales Performance Analytics is a data analytics project that examines sales, profit, orders, product performance, customer segments, and regional trends. Python is used for analysis, while Power BI is used to present findings in dashboards.

## Objectives

- Measure overall sales and profitability.
- Explore monthly sales trends.
- Compare performance across product categories, regions, and customer segments.
- Identify top-selling products and products with negative profit.
- Examine the relationship between discounts and profit.
- Present findings through Power BI dashboards.

## Tools and Technologies

- **Python** — analysis and calculations
- **Pandas** — data loading and manipulation
- **Matplotlib** — charts and visualizations
- **Power BI** — interactive dashboards
- **DAX** — KPI measures
- **Git and GitHub** — version control and project sharing

## Project Structure

```text
Business-Sales-Performance-Analytics/
├── dataset/
│   └── sales_data.csv
├── python/
│   └── sales_analysis.py
├── powerbi/
│   └── Business_Sales_Dashboard.pbix
├── screenshots/
│   ├── executive_overview.png
│   ├── sales_analysis.png
│   └── profit_analysis.png
└── README.md
```

*Adjust the folder and screenshot names above if your actual files use different names.*

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Total Quantity Sold | 37,873 |
| Average Order Value | $458.61 |
| Profit Margin | 12.47% |

## Dashboard Pages

### 1. Executive Overview
Summarizes the main KPIs: sales, profit, order count, average order value, profit margin, and quantity sold.

### 2. Sales Analysis
Includes monthly sales trends and comparisons by category, region, customer segment, sub-category, and top products by sales.

### 3. Profit Analysis
Examines profit by category and region, the relationship between discount and profit, and products with the lowest profit.

## Key Insights

- **Category performance:** Technology generated approximately $836,154 in sales and $145,455 in profit.
- **Regional performance:** The West region generated approximately $725,458 in sales and $108,418 in profit.
- **Customer segments:** The Consumer segment generated approximately $1,161,401 in sales, the highest of the three segments.
- **Top product:** The Canon imageCLASS 2200 Advanced Copier generated approximately $61,599.82 in sales and $25,199.93 in profit.
- **Loss-making products:** The Cubify CubeX 3D Printer Double Head Print recorded an approximate loss of $8,879.97.
- **Discount and profit:** The observed correlation between discount and profit was approximately -0.219, indicating a weak negative association. Correlation alone does not establish causation.

## Recommendations

- Review the pricing, costs, and discounting of loss-making products.
- Study the sales approaches used in high-performing regions and categories.
- Monitor monthly sales to support inventory and sales planning.
- Evaluate promotions using both sales volume and profitability.
- Use the dashboard to track KPIs and guide business decisions.

## How to Run the Python Analysis

1. Install Python.
2. Open a terminal in the project root directory.
3. Install the required packages:

   ```bash
   pip install pandas matplotlib
   ```

4. Run the analysis script:

   ```bash
   python python/sales_analysis.py
   ```

Ensure the script's CSV path matches the location of `sales_data.csv`.

## Open the Power BI Dashboard

Open `powerbi/Business_Sales_Dashboard.pbix` in Power BI Desktop. If the dataset has moved, update the data source path when prompted.

## Dashboard Screenshots

If screenshots are available, store them in the `screenshots/` folder and add them here. Update the filenames to match your actual screenshots.

![Executive Overview](screenshots/executive_overview.png)

![Sales Analysis](screenshots/sales_analysis.png)

![Profit Analysis](screenshots/profit_analysis.png)

## Skills Demonstrated

- Data cleaning and preparation
- Exploratory data analysis
- KPI calculation
- Data visualization
- Power BI dashboard development
- DAX measures
- Business insight generation
- Analytical reporting

## Conclusion

This project demonstrates how Python and Power BI can be combined to analyze sales performance, compare profitability across business dimensions, identify products that may need attention, and communicate findings through dashboards.

**Project type:** Data Analytics / Business Intelligence  
**Tools:** Python, Pandas, Matplotlib, Power BI, DAX
