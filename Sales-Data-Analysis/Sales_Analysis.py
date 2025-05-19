Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_excel('/Users/Omkar/Desktop/Data Sales/Walmart_Sales_Cleaned.xlsx')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Week'] = df['Date'].dt.isocalendar().week

monthly_sales = df.groupby(['Year', 'Month'])['Weekly_Sales'].sum().reset_index()
monthly_sales['Month_Year'] = monthly_sales['Month'].astype(str) + '-' + monthly_sales['Year'].astype(str)

plt.figure(figsize=(10,6))
<Figure size 2000x1200 with 0 Axes>
plt.plot(monthly_sales['Month_Year'], monthly_sales['Weekly_Sales'], marker='o', color='b')
[<matplotlib.lines.Line2D object at 0x10d2b5590>]
plt.title('Monthly Sales Trend')
Text(0.5, 1.0, 'Monthly Sales Trend')
plt.xlabel('Month-Year')
Text(0.5, 0, 'Month-Year')
plt.ylabel('Total Weekly Sales')
Text(0, 0.5, 'Total Weekly Sales')
plt.xticks(rotation=45)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [Text(0, 0, '1-2010'), Text(1, 0, '2-2010'), Text(2, 0, '3-2010'), Text(3, 0, '4-2010'), Text(4, 0, '5-2010'), Text(5, 0, '6-2010'), Text(6, 0, '7-2010'), Text(7, 0, '8-2010'), Text(8, 0, '9-2010'), Text(9, 0, '10-2010'), Text(10, 0, '11-2010'), Text(11, 0, '12-2010'), Text(12, 0, '1-2011'), Text(13, 0, '2-2011'), Text(14, 0, '3-2011'), Text(15, 0, '4-2011'), Text(16, 0, '5-2011'), Text(17, 0, '6-2011'), Text(18, 0, '7-2011'), Text(19, 0, '8-2011'), Text(20, 0, '9-2011'), Text(21, 0, '10-2011'), Text(22, 0, '11-2011'), Text(23, 0, '12-2011'), Text(24, 0, '1-2012'), Text(25, 0, '2-2012'), Text(26, 0, '3-2012'), Text(27, 0, '4-2012'), Text(28, 0, '5-2012'), Text(29, 0, '6-2012'), Text(30, 0, '7-2012'), Text(31, 0, '8-2012'), Text(32, 0, '9-2012'), Text(33, 0, '10-2012'), Text(34, 0, '11-2012'), Text(35, 0, '12-2012')])
>>> plt.grid(True)
>>> plt.tight_layout()
>>> 
>>> plt.show()
>>> 
>>> plt.show()
>>> df_sorted = df.sort_values('Date')
>>> plt.figure(figsize=(10,6))
... 
<Figure size 2000x1200 with 0 Axes>
>>> plt.plot(df_sorted['Date'], df_sorted['Temperature'], color='orange')
[<matplotlib.lines.Line2D object at 0x10d34afd0>]
>>> plt.title('Temperature Trend Over Time')
Text(0.5, 1.0, 'Temperature Trend Over Time')
>>> plt.xlabel('Date')
Text(0.5, 0, 'Date')
>>> plt.ylabel('Temperature (°F)')
Text(0, 0.5, 'Temperature (°F)')
>>> plt.grid(True)
>>> plt.tight_layout()
>>> 
>>> plt.show()
>>> 
>>> plt.figure(figsize=(8,6))
<Figure size 1600x1200 with 0 Axes>
>>> plt.scatter(df['Temperature'], df['Weekly_Sales'], alpha=0.6, color='purple')
<matplotlib.collections.PathCollection object at 0x10cf263c0>
>>> plt.title('Temperature vs Weekly Sales')
Text(0.5, 1.0, 'Temperature vs Weekly Sales')
>>> plt.xlabel('Temperature (°F)')
Text(0.5, 0, 'Temperature (°F)')
>>> plt.ylabel('Weekly Sales')
Text(0, 0.5, 'Weekly Sales')
>>> plt.grid(True)
>>> plt.tight_layout()
>>> plt.show()
>>> 
>>> 
>>> plt.figure(figsize=(10,6))
<Figure size 2000x1200 with 0 Axes>
>>> plt.plot(df_sorted['Date'], df_sorted['Fuel_Price'], color='green')
[<matplotlib.lines.Line2D object at 0x1256c8910>]
>>> plt.title('Fuel Price Trend Over Time')
Text(0.5, 1.0, 'Fuel Price Trend Over Time')
>>> plt.xlabel('Date')
Text(0.5, 0, 'Date')
>>> plt.ylabel('Fuel Price ($)')
Text(0, 0.5, 'Fuel Price ($)')
>>> plt.grid(True)
>>> plt.tight_layout()
>>> 
>>> plt.show()
