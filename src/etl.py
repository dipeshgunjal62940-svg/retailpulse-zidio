from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
CLEANED_DIR = DATA_DIR / "cleaned"
DEMO_DIR = DATA_DIR / "demo"

def load_data():
    """Load all Zidio project CSV files."""
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    DEMO_DIR.mkdir(parents=True, exist_ok=True)
    
    print("Loading Zidio datasets...")
    sales_df = pd.read_csv(PROJECT_ROOT / "sales_sample.csv")
    customer_df = pd.read_csv(PROJECT_ROOT / "customer_master.csv")
    sku_df = pd.read_csv(PROJECT_ROOT / "sku_master.csv")
    store_df = pd.read_csv(PROJECT_ROOT / "store_master.csv")
    promo_df = pd.read_csv(PROJECT_ROOT / "promotions.csv")
    inventory_df = pd.read_csv(PROJECT_ROOT / "inventory_snapshot.csv")
    
    return sales_df, customer_df, sku_df, store_df, promo_df, inventory_df

def main():
    try:
        sales_df, customer_df, sku_df, store_df, promo_df, inventory_df = load_data()
        
        print(f"Sales rows loaded: {sales_df.shape[0]:,}")
        
        # 1. Cleaning & Processing
        sales_df['date'] = pd.to_datetime(sales_df['date'], errors='coerce')
        sales_df = sales_df[(sales_df['quantity'] > 0) & (sales_df['unit_price'] >= 0)]
        sales_df['promo_id'] = sales_df['promo_id'].fillna('NO_PROMO')
        
        # 2. Privacy & Anonymization (Zidio requirement)
        sales_df['customer_id_masked'] = sales_df['customer_id'].apply(
            lambda x: f"CUST_ANON_{str(x)[-4:]}" if pd.notnull(x) else "CUST_UNKNOWN"
        )
        
        # Save cleaned main sales file
        cleaned_path = CLEANED_DIR / "cleaned_sales.csv"
        sales_df.to_csv(cleaned_path, index=False)
        print(f"Cleaned sales saved to: {cleaned_path}")
        
        # 3. Generate Dashboard Demo Tables (Fast loading for Streamlit under 8s)
        # - Daily sales summary
        daily_sales = sales_df.groupby(['date', 'store_id']).agg(
            total_revenue=('total_value', 'sum'),
            total_quantity=('quantity', 'sum'),
            total_transactions=('receipt_id', 'nunique')
        ).reset_index()
        daily_sales.to_csv(DEMO_DIR / "daily_sales_summary.csv", index=False)
        
        # - Customer RFM features for Segmentation team
        max_date = sales_df['date'].max()
        rfm = sales_df.groupby('customer_id').agg(
            recency=('date', lambda x: (max_date - x.max()).days),
            frequency=('receipt_id', 'nunique'),
            monetary=('total_value', 'sum')
        ).reset_index()
        rfm.to_csv(DEMO_DIR / "customer_rfm.csv", index=False)
        
        print("Demo summary tables generated successfully in data/demo/!")

    except Exception as error:
        print(f"Error during ETL execution: {error}")

if __name__ == "__main__":
    main()
