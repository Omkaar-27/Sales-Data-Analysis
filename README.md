# Sales-Data-Analysis
A sales data analytics project using Python, Excel, and Matplotlib

# Sales Data Analysis

This project presents a time-series analysis of Walmart sales data using Python and Excel. It includes data processing, visual exploration of trends, and breakdowns based on various factors like temperature and fuel prices.

## Tools & Technologies

- Python (pandas, matplotlib)
- Excel / Google Sheets
- Jupyter Notebook / IDLE
- GitHub for version control

## Features

- Monthly sales trend analysis
- Temperature trend visualization
- Fuel price trend visualization
- Organized plots for quick insights

## Dataset Overview

**Filename:** `Walmart_Sales_Cleaned.xlsx`

| Column Name     | Description                                |
|-----------------|--------------------------------------------|
| Store           | Store ID                                   |
| Date            | Weekly date of record                      |
| Weekly_Sales    | Total sales for the week                   |
| Holiday_Flag    | Indicates if the week contained a holiday  |
| Temperature     | Average temperature that week (in °F)      |
| Fuel_Price      | Fuel price (in USD)                        |
| CPI             | Consumer Price Index                       |
| Unemployment    | Unemployment rate                          |

## Sample Visualizations

### Monthly Sales Trend

![Montly_Sales_Trend](https://github.com/user-attachments/assets/f2e81f6b-eacc-4fe6-86a6-06063d76e5af)

### Temperature Over Time
![Temperature_Trend_Over_Time](https://github.com/user-attachments/assets/d1d5acca-3cd4-4be5-8374-f24e1b41e165)


### Fuel Price Trend
![Fuel_Price_Trend_Over_Time](https://github.com/user-attachments/assets/7c03244a-d095-4c20-b4e6-36d46b2d70de)


## How to Run

1. Install the required libraries:

   ```bash
   pip install pandas matplotlib openpyxl

