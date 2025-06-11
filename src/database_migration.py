import oracledb
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection using environment variable for password
dsn = oracledb.makedsn("127.0.0.1", 1521, service_name="XE")
connection = oracledb.connect(user="system", password=os.environ.get("ORACLE_PASSWORD"), dsn=dsn)
cursor = connection.cursor()

# Load data
reviews_df = pd.read_csv("data/bank_reviews.csv")

# Insert into banks
banks = reviews_df['bank'].unique()
for bank_id, bank_name in enumerate(banks, start=1):
    cursor.execute("INSERT INTO banks (bank_id, bank_name) VALUES (:1, :2)", (bank_id, bank_name))

# Insert into reviews
for index, row in reviews_df.iterrows():
    try:
        # Validate numeric columns
        review_id = int(row['review_id']) if pd.notna(row['review_id']) else None
        rating = int(row['rating']) if pd.notna(row['rating']) else None
        bank_id = list(reviews_df['bank'].unique()).index(row['bank']) + 1
        
        # Handle review column
        review_value = row['review'][:1000] if pd.notna(row['review']) else None
        
        # Skip rows with invalid numeric data
        if review_id is None or rating is None:
            print(f"Skipping row {index} due to invalid data: {row.to_dict()}")
            continue
        
        # Insert into database
        cursor.execute("""
            INSERT INTO reviews (review_id, review, rating, review_date, bank_id, source)
            VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5, :6)
        """, (review_id, review_value, rating, row['date'], bank_id, row['source']))
    except Exception as e:
        print(f"Error at row {index}: {e}")
        raise

# Commit and close
connection.commit()
cursor.close()
connection.close()
print("Data migrated to Oracle database successfully.")