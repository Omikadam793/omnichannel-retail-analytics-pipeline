-- Query 1: Running Cumulative Revenue Growth Tracking (Day 2 Window Functions!)
SELECT 
    Order_Date,
    Region,
    Sales_Revenue,
    SUM(Sales_Revenue) OVER(PARTITION BY Region ORDER BY Order_Date) AS Cumulative_Regional_Revenue
FROM fct_sales;

-- Query 2: Segment Rank Deep Dive (CTEs + Dense Rank)
WITH SegmentRevenueCTE AS (
    SELECT 
        Region,
        Customer_Segment,
        SUM(Sales_Revenue) AS Total_Revenue,
        SUM(Net_Profit) AS Total_Profit
    FROM fct_sales
    GROUP BY Region, Customer_Segment
)
SELECT 
    Region,
    Customer_Segment,
    Total_Revenue,
    Total_Profit,
    DENSE_RANK() OVER(PARTITION BY Region ORDER BY Total_Revenue DESC) AS Revenue_Rank
FROM SegmentRevenueCTE;