import pandas as pd
import sqlite3

# 1. Load the cleaned data
print("Loading cleaned data into SQLite...")
df = pd.read_csv('data/cleaned/superstore_cleaned.csv')

# 2. Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
df.to_sql('orders', conn, index=False, if_exists='replace')

# 3. Define the queries (matching your .sql file)
queries = {
    "1. Total Revenue and Profit": """
        SELECT 
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit,
            ROUND(AVG("Profit Margin"), 2) AS Avg_Profit_Margin
        FROM orders;
    """,
    "2. Sales by Region": """
        SELECT 
            Region,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit
        FROM orders
        GROUP BY Region
        ORDER BY Total_Sales DESC;
    """,
    "3. Sales by Category": """
        SELECT 
            Category,
            ROUND(SUM(Sales), 2) AS Total_Sales,
            ROUND(SUM(Profit), 2) AS Total_Profit
        FROM orders
        GROUP BY Category
        ORDER BY Total_Sales DESC;
    """,
    "4. Top 10 Sub-Categories by Revenue": """
        SELECT 
            "Sub-Category",
            ROUND(SUM(Sales), 2) AS Total_Revenue,
            ROUND(SUM(Profit), 2) AS Total_Profit
        FROM orders
        GROUP BY "Sub-Category"
        ORDER BY Total_Revenue DESC
        LIMIT 10;
    """,
    "5. Discount Impact on Profit": """
        SELECT 
            CASE 
                WHEN Discount = 0 THEN 'No Discount'
                WHEN Discount <= 0.1 THEN '0-10%'
                WHEN Discount <= 0.2 THEN '10-20%'
                WHEN Discount <= 0.3 THEN '20-30%'
                ELSE '30%+'
            END AS Discount_Bucket,
            COUNT(*) AS Order_Count,
            ROUND(AVG(Profit), 2) AS Avg_Profit,
            ROUND(AVG("Profit Margin"), 2) AS Avg_Margin
        FROM orders
        GROUP BY Discount_Bucket
        ORDER BY Avg_Profit DESC;
    """
}

# 4. Execute and display each query result
for title, sql in queries.items():
    print(f"\n{'='*50}")
    print(f"📊 {title}")
    print(f"{'='*50}")
    result = pd.read_sql_query(sql, conn)
    print(result.to_string(index=False))

# 5. Close the connection
conn.close()
print("\n✅ SQL Analysis Complete!")