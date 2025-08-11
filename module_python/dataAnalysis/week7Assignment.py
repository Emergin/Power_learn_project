# Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
# Load the dataset using pandas.
# Display the first few rows of the dataset using .head() to inspect the data.
# Explore the structure of the dataset by checking the data types and any missing values.
# Clean the dataset by either filling or dropping any missing values.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('/home/trubel/Documents/Github/Power_learn_project/module_python/pythonLibraries/sales_data_sample.csv', encoding='latin-1')
# print(df.head(5))
# print(df.info())
# print(df.isnull().sum())
df_cleaned = df.drop(['ADDRESSLINE2', 'STATE'], axis=1)
df_cleaned['POSTALCODE'] = df_cleaned['POSTALCODE'].fillna('Unknown')
df_cleaned['TERRITORY'] = df_cleaned['TERRITORY'].fillna('Unknown')
# print(f"Total missing values: {df_cleaned.isnull().sum().sum()}")
# Verify cleaning
if df_cleaned.isnull().sum().sum() == 0:
    print("✓ Dataset successfully cleaned - no missing values!")
else:
    print("⚠ Still has missing values")

# Show first few rows
# print(df_cleaned.head())


# TASK 2 
# Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
# Perform groupings on a categorical column (for example, species, region, or department) 
# and compute the mean of a numerical column for each group.
# Identify any patterns or interesting findings from your analysis.

numerical_stats = df_cleaned.describe()
# print(numerical_stats)

productline_sales = df_cleaned.groupby('PRODUCTLINE')['SALES'].mean().sort_values(ascending=False)
print(productline_sales)

# group by country and compute mean sales 
country_sales = df_cleaned.groupby('COUNTRY')['SALES'].mean().sort_values(ascending=False)
print(country_sales)

# group by status and compute mean sales 
status_sales = df_cleaned.groupby('STATUS')['SALES'].mean()
print(status_sales)

# top performing categories 
productline_analysis = df_cleaned.groupby('PRODUCTLINE').agg({'SALES': ['count', 'mean', 'sum'],'QUANTITYORDERED': 'mean'}).round(2)
productline_analysis.columns = ['Order_Count', 'Avg_Sale', 'Total_Sales', 'Avg_Quantity']
productline_analysis = productline_analysis.sort_values('Total_Sales', ascending=False)
print(productline_analysis)

# 2. GEOGRAPHIC PERFORMANCE
print("\n🌍 2. GEOGRAPHIC PERFORMANCE:")
print("-" * 40)
country_analysis = df_cleaned.groupby('COUNTRY').agg({
    'SALES': ['count', 'mean', 'sum']
}).round(2)
country_analysis.columns = ['Order_Count', 'Avg_Sale', 'Total_Sales']
country_analysis = country_analysis.sort_values('Total_Sales', ascending=False)
print(country_analysis.head(10))

# 3. DEAL SIZE ANALYSIS
print("\n💰 3. DEAL SIZE PATTERNS:")
print("-" * 40)
dealsize_analysis = df_cleaned.groupby('DEALSIZE').agg({
    'SALES': ['count', 'mean', 'min', 'max'],
    'PRICEEACH': 'mean',
    'QUANTITYORDERED': 'mean'
}).round(2)
print(dealsize_analysis)

# 4. SEASONAL PATTERNS
print("\n📅 4. SEASONAL/TEMPORAL PATTERNS:")
print("-" * 40)
# Monthly analysis
monthly_sales = df_cleaned.groupby('MONTH_ID')['SALES'].agg(['count', 'mean', 'sum']).round(2)
monthly_sales.columns = ['Order_Count', 'Avg_Sale', 'Total_Sales']
print("Monthly Performance:")
print(monthly_sales)

# Quarterly analysis
quarterly_sales = df_cleaned.groupby('QTR_ID')['SALES'].agg(['count', 'mean', 'sum']).round(2)
quarterly_sales.columns = ['Order_Count', 'Avg_Sale', 'Total_Sales']
print("\nQuarterly Performance:")
print(quarterly_sales)

# 5. CUSTOMER ANALYSIS
print("\n👥 5. TOP CUSTOMERS:")
print("-" * 40)
customer_analysis = df_cleaned.groupby('CUSTOMERNAME').agg({
    'SALES': ['count', 'sum']
}).round(2)
customer_analysis.columns = ['Order_Count', 'Total_Sales']
customer_analysis = customer_analysis.sort_values('Total_Sales', ascending=False)
print(customer_analysis.head(10))

# 6. PRICE vs QUANTITY RELATIONSHIP
print("\n📈 6. PRICE vs QUANTITY INSIGHTS:")
print("-" * 40)
price_ranges = pd.cut(df_cleaned['PRICEEACH'], bins=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
price_quantity = df_cleaned.groupby(price_ranges).agg({'QUANTITYORDERED': 'mean','SALES': 'mean'}).round(2)
print(price_quantity)

# 7. ORDER STATUS ANALYSIS
print("\n📋 7. ORDER STATUS PATTERNS:")
print("-" * 40)
status_analysis = df_cleaned.groupby('STATUS').agg({
    'SALES': ['count', 'mean', 'sum'],
    'ORDERNUMBER': 'nunique'
}).round(2)
status_analysis.columns = ['Order_Count', 'Avg_Sale', 'Total_Sales', 'Unique_Orders']
print(status_analysis)

# 8. KEY INSIGHTS SUMMARY
print("\n🎯 KEY FINDINGS & PATTERNS:")
print("=" * 60)

# Find top performers
top_productline = productline_analysis.index[0]
top_country = country_analysis.index[0]
best_quarter = quarterly_sales['Total_Sales'].idxmax()
best_month = monthly_sales['Total_Sales'].idxmax()

print(f"🏆 Top Product Line: {top_productline}")
print(f"🌟 Best Performing Country: {top_country}")
print(f"📅 Strongest Quarter: Q{best_quarter}")
print(f"📆 Best Month: Month {best_month}")
print(f"💎 Average Deal Size: ${df_cleaned['SALES'].mean():.2f}")
print(f"📊 Total Revenue: ${df_cleaned['SALES'].sum():,.2f}")
print(f"🛒 Total Orders: {len(df_cleaned)}")

# Statistical insights
print(f"\n📈 STATISTICAL INSIGHTS:")
print(f"• Sales Range: ${df_cleaned['SALES'].min():.2f} - ${df_cleaned['SALES'].max():,.2f}")
print(f"• Price Range: ${df_cleaned['PRICEEACH'].min():.2f} - ${df_cleaned['PRICEEACH'].max():.2f}")
print(f"• Quantity Range: {df_cleaned['QUANTITYORDERED'].min()} - {df_cleaned['QUANTITYORDERED'].max()} units")
print(f"• Standard Deviation in Sales: ${df_cleaned['SALES'].std():.2f}")

# Correlation insights
correlation_matrix = df_cleaned[['SALES', 'QUANTITYORDERED', 'PRICEEACH']].corr()
print(f"\n🔗 CORRELATIONS:")
print(f"• Sales vs Quantity Ordered: {correlation_matrix.loc['SALES', 'QUANTITYORDERED']:.3f}")
print(f"• Sales vs Price Each: {correlation_matrix.loc['SALES', 'PRICEEACH']:.3f}")
print(f"• Price vs Quantity: {correlation_matrix.loc['PRICEEACH', 'QUANTITYORDERED']:.3f}")



# TASK 3
# Create at least four different types of visualizations:
# Line chart showing trends over time (for example, a time-series of sales data).
# Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
# Histogram of a numerical column to understand its distribution.
# Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
# Customize your plots with titles, labels for axes, and legends where necessary.

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

fig = plt.figure(figsize=(16, 12))

# 1 line chart
plt.subplot(2,2,1)
monthly_sales = df_cleaned.groupby('MONTH_ID')['SALES'].sum().reset_index()
plt.plot(monthly_sales['MONTH_ID'], monthly_sales['SALES'], marker='o', linewidth=2.5, markersize=8, color='#2E86AB')
plt.title('Monthly sales trends', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(range(1, 13))

# Format y-axis to show values in thousands
ax1 = plt.gca()
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# 2. BAR CHART - Average sales by product line
plt.subplot(2, 2, 2)
productline_avg = df_cleaned.groupby('PRODUCTLINE')['SALES'].mean().sort_values(ascending=True)
colors = plt.cm.Set3(np.linspace(0, 1, len(productline_avg)))
bars = plt.barh(range(len(productline_avg)), productline_avg.values, color=colors)
plt.title('🏆 Average Sales by Product Line', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Average Sales ($)', fontsize=12)
plt.ylabel('Product Line', fontsize=12)
plt.yticks(range(len(productline_avg)), productline_avg.index)

# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars, productline_avg.values)):
    plt.text(value + 100, i, f'${value:.0f}', va='center', fontsize=10)

plt.tight_layout()

# 3. HISTOGRAM - Distribution of sales values
plt.subplot(2, 2, 3)
plt.hist(df_cleaned['SALES'], bins=30, color='#A23B72', alpha=0.7, edgecolor='black', linewidth=0.5)
plt.title('📊 Distribution of Sales Values', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Sales Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')

# Add statistics text
mean_sales = df_cleaned['SALES'].mean()
median_sales = df_cleaned['SALES'].median()
plt.axvline(mean_sales, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_sales:.0f}')
plt.axvline(median_sales, color='orange', linestyle='--', linewidth=2, label=f'Median: ${median_sales:.0f}')
plt.legend()

# 4. SCATTER PLOT - Relationship between Price and Quantity Ordered
plt.subplot(2, 2, 4)
scatter = plt.scatter(df_cleaned['PRICEEACH'], df_cleaned['QUANTITYORDERED'], 
                     c=df_cleaned['SALES'], cmap='viridis', alpha=0.6, s=50)
plt.title('💰 Price vs Quantity Ordered\n(Color = Sales Amount)', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Price Each ($)', fontsize=12)
plt.ylabel('Quantity Ordered', fontsize=12)
plt.grid(True, alpha=0.3)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Sales Amount ($)', fontsize=10)

# Add trend line
z = np.polyfit(df_cleaned['PRICEEACH'], df_cleaned['QUANTITYORDERED'], 1)
p = np.poly1d(z)
plt.plot(df_cleaned['PRICEEACH'].sort_values(), p(df_cleaned['PRICEEACH'].sort_values()), 
         "r--", alpha=0.8, linewidth=2, label=f'Trend Line')
plt.legend()

plt.tight_layout()
plt.show()

# Additional visualizations for deeper insights
fig2, axes = plt.subplots(2, 2, figsize=(16, 10))

# 5. QUARTERLY SALES COMPARISON (Bar Chart)
quarterly_sales = df_cleaned.groupby('QTR_ID')['SALES'].sum()
axes[0, 0].bar(quarterly_sales.index, quarterly_sales.values, 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
axes[0, 0].set_title('📅 Quarterly Sales Performance', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Quarter')
axes[0, 0].set_ylabel('Total Sales ($)')
axes[0, 0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000000:.1f}M'))

# Add value labels on bars
for i, v in enumerate(quarterly_sales.values):
    axes[0, 0].text(i+1, v + 50000, f'${v/1000000:.1f}M', ha='center', fontweight='bold')

# 6. TOP 10 COUNTRIES BY SALES (Horizontal Bar Chart)
top_countries = df_cleaned.groupby('COUNTRY')['SALES'].sum().nlargest(10)
axes[0, 1].barh(range(len(top_countries)), top_countries.values, 
                color=plt.cm.plasma(np.linspace(0, 1, len(top_countries))))
axes[0, 1].set_title('🌍 Top 10 Countries by Total Sales', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Total Sales ($)')
axes[0, 1].set_yticks(range(len(top_countries)))
axes[0, 1].set_yticklabels(top_countries.index)
axes[0, 1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))

# 7. DEAL SIZE DISTRIBUTION (Pie Chart)
dealsize_counts = df_cleaned['DEALSIZE'].value_counts()
colors_pie = ['#FF9999', '#66B2FF', '#99FF99']
wedges, texts, autotexts = axes[1, 0].pie(dealsize_counts.values, labels=dealsize_counts.index, 
                                          autopct='%1.1f%%', colors=colors_pie, startangle=90)
axes[1, 0].set_title('💎 Distribution of Deal Sizes', fontsize=14, fontweight='bold')

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# 8. CORRELATION HEATMAP
numeric_cols = ['SALES', 'QUANTITYORDERED', 'PRICEEACH', 'MONTH_ID', 'QTR_ID']
correlation_matrix = df_cleaned[numeric_cols].corr()

im = axes[1, 1].imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
axes[1, 1].set_title('🔗 Correlation Matrix', fontsize=14, fontweight='bold')
axes[1, 1].set_xticks(range(len(numeric_cols)))
axes[1, 1].set_yticks(range(len(numeric_cols)))
axes[1, 1].set_xticklabels(numeric_cols, rotation=45)
axes[1, 1].set_yticklabels(numeric_cols)

# Add correlation values as text
for i in range(len(numeric_cols)):
    for j in range(len(numeric_cols)):
        text = axes[1, 1].text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}',
                              ha="center", va="center", color="black", fontweight='bold')

# Add colorbar for correlation
cbar2 = plt.colorbar(im, ax=axes[1, 1])
cbar2.set_label('Correlation Coefficient')

plt.tight_layout()
plt.show()

# Print insights about the visualizations
print("🎨 VISUALIZATION INSIGHTS:")
print("=" * 50)
print("1. 📈 LINE CHART (Monthly Trends):")
best_month = monthly_sales.loc[monthly_sales['SALES'].idxmax(), 'MONTH_ID']
print(f"   • Peak sales occurred in Month {best_month}")
print(f"   • Shows clear seasonal patterns in sales performance")

print("\n2. 🏆 BAR CHART (Product Line Performance):")
top_product = productline_avg.index[-1]
print(f"   • {top_product} has the highest average sales")
print(f"   • Clear performance hierarchy among product lines")

print("\n3. 📊 HISTOGRAM (Sales Distribution):")
print(f"   • Sales are right-skewed with mean ${mean_sales:.0f} > median ${median_sales:.0f}")
print(f"   • Most sales fall in the lower range with few high-value outliers")

print("\n4. 💰 SCATTER PLOT (Price vs Quantity):")
correlation = df_cleaned['PRICEEACH'].corr(df_cleaned['QUANTITYORDERED'])
print(f"   • Correlation between price and quantity: {correlation:.3f}")
if correlation < -0.3:
    print("   • Strong negative correlation: higher prices → lower quantities")
elif correlation > 0.3:
    print("   • Strong positive correlation: higher prices → higher quantities")
else:
    print("   • Weak correlation between price and quantity")

print(f"\n📊 Dataset Summary:")
print(f"   • Total Records: {len(df_cleaned):,}")
print(f"   • Date Range: {df_cleaned['YEAR_ID'].min()} - {df_cleaned['YEAR_ID'].max()}")
print(f"   • Countries: {df_cleaned['COUNTRY'].nunique()}")
print(f"   • Product Lines: {df_cleaned['PRODUCTLINE'].nunique()}")
print(f"   • Total Revenue: ${df_cleaned['SALES'].sum():,.2f}")
