import pandas as pd

try:
    df = pd.read_csv("data/bank_reviews.csv", encoding='utf-8')
    print("CSV loaded successfully. Total rows:", len(df))
    # Check for non-numeric values in numeric columns
    invalid_review_id = df[~df['review_id'].astype(str).str.match(r'^\d+$', na=False)]
    invalid_rating = df[~df['rating'].astype(str).str.match(r'^\d*\.?\d+$', na=False)]  # Allows decimals
    invalid_bank_id = df[~df['bank_id'].astype(str).str.match(r'^\d+$', na=False)] if 'bank_id' in df else pd.DataFrame()
    if not invalid_review_id.empty:
        print("Invalid review_id rows:\n", invalid_review_id)
    else:
        print("No invalid review_id values found.")
    if not invalid_rating.empty:
        print("Invalid rating rows:\n", invalid_rating)
    else:
        print("No invalid rating values found.")
    if not invalid_bank_id.empty:
        print("Invalid bank_id rows:\n", invalid_bank_id)
    else:
        print("No invalid bank_id values found (or column not present).")
except FileNotFoundError:
    print("Error: data/bank_reviews.csv not found.")
except Exception as e:
    print(f"Error: {e}")