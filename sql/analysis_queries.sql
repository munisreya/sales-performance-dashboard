-- 1. Total Revenue, Profit, and Average Margin
SELECT 
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG("Profit Margin"), 2) AS Avg_Profit_Margin
FROM orders;

-- 2. Sales and Profit by Region
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG("Profit Margin"), 2) AS Avg_Margin
FROM orders
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 3. Sales and Profit by Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 4. Top 10 Sub-Categories by Revenue
SELECT 
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS Total_Revenue,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY "Sub-Category"
ORDER BY Total_Revenue DESC
LIMIT 10;

-- 5. Discount Impact on Profit
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

-- 6. Sales by Customer Segment
SELECT 
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(*) AS Order_Count
FROM orders
GROUP BY Segment
ORDER BY Total_Sales DESC;