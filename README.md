 # 🛒 RetailPulse: AI-Powered Customer Analytics & Demand Forecasting Platform
**Zidio Data Analytics & ETL Project (Submission Deadline: 20 October 2026)**

---

## 📌 Project Overview
RetailPulse is an enterprise-grade retail analytics platform designed to process, clean, and analyze a massive dataset of nearly **10 million transactions** ($9,972,038$ rows). The platform provides crucial insights into sales performance, customer purchasing behavior (RFM), inventory management, and demand forecasting across multiple stores and SKUs.

---

## 👥 Team & Responsibilities
* **Data & ETL Lead:** Dipesh Gunjal (Pipeline architecture, data cleaning, masking, and repository management)
* **Dashboard Lead (Role D):** Visualization & Streamlit deployment using pre-aggregated demo tables
* **Segmentation Lead (Role B):** Customer RFM analysis and clustering models
* **Forecasting Lead (Role C):** Time-series sales prediction and inventory optimization

---

## 📂 Project Directory Structure
```text
retailpulse-zidio/
│
├── data/
│   ├── cleaned/             # Processed datasets (e.g., cleaned_sales.csv)
│   └── demo/                # Pre-aggregated summary tables for fast dashboard rendering
│       ├── daily_sales_summary.csv
│       ├── customer_rfm.csv
│       └── inventory_summary.csv
│
├── src/
│   └── etl.py               # Core ETL pipeline script
│
├── .gitignore               # Strict data privacy & ignore rules
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation