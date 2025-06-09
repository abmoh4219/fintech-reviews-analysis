from google_play_scraper import reviews_all
import pandas as pd
import os

# Define banks and their app IDs (replace with actual IDs from Google Play Store)
banks = [
    {"name": "Commercial Bank of Ethiopia", "app_id": "com.combanketh.mobilebanking", "source": "Google Play"},
    {"name": "Bank of Abyssinia", "app_id": "com.boa.boaMobileBanking", "source": "Google Play"},
    {"name": "Dashen Bank", "app_id": "com.dashen.dashensuperapp", "source": "Google Play"}
]

# Scrape reviews
all_reviews = []
for bank in banks:
    print(f"Scraping reviews for {bank['name']}...")
    reviews = reviews_all(
        bank["app_id"],
        lang="en",
        country="et",
        count=400
    )
    for review in reviews:
        review["bank"] = bank["name"]
        review["source"] = bank["source"]
    all_reviews.extend(reviews)

# Convert to DataFrame
df = pd.DataFrame(all_reviews)

# Preprocess data
df = df[["content", "score", "at", "bank", "source"]].rename(
    columns={"content": "review", "score": "rating", "at": "date"}
)
df.drop_duplicates(subset=["review"], inplace=True)
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
df["review_id"] = range(1, len(df) + 1)

# Save to CSV
output_file = "data/bank_reviews.csv"  # Updated to save in data/ folder
df.to_csv(output_file, index=False)
print(f"Saved {len(df)} reviews to {output_file}")