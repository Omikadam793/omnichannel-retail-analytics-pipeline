# End-to-End Omnichannel Retail Analytics Pipeline

## 📊 Business Scenario
Executive stakeholders required an automated solution to ingest raw, messy e-commerce sales streams, standardize structural datatypes, isolate performance leaks via metrics tracking, and surface interactive global market trends.

## 🏗️ System Architecture
1. **Extraction:** Raw multi-dimensional transaction logs are isolated from a mock file stream pipeline.
2. **Transformation (Python / Pandas):** Handled string trimming, numeric type coercion, missing value median/zero imputation, and engineered high-value purchase indicator flags via NumPy.
3. **Storage & Warehousing (SQL):** Extracted rows are loaded into a relational warehouse database using a structured schema layer.
4. **Analysis (Advanced SQL):** Executed advanced analytical data views using Window Functions, CTEs, and Partitioned Dense Rankings.
5. **Business Intelligence (Power BI):** Modeled formal DAX metrics to track Total Sales Revenue, Net Profits, and Profit Margins over dynamic regional time-series dimensions.

## 🚀 How To Run The Pipeline
```bash
# Clone the repository
git clone [https://github.com/Omikadam793/omnichannel-retail-analytics-pipeline.git](https://github.com/Omikadam793/omnichannel-retail-analytics-pipeline.git)

# Run the complete data pipeline ingestion script
python scripts/data_pipeline.py