import pandas as pd
from textblob import TextBlob

# Load reviews
df = pd.read_csv("data/bank_reviews.csv")

# Check available columns (for debugging)
print("Available columns:", df.columns.tolist())

# Sentiment analysis
df["sentiment_score"] = df["review"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df["sentiment_label"] = df["sentiment_score"].apply(
    lambda x: "positive" if x > 0 else "negative" if x < 0 else "neutral"
)

# Simple keyword extraction
def extract_keywords(text):
    words = str(text).lower().split()
    common_keywords = ["crash", "login", "slow", "ui", "transfer", "support"]
    return [word for word in words if word in common_keywords]

df["keywords"] = df["review"].apply(extract_keywords)

# Group by bank and identify themes
themes = {
    "Commercial Bank of Ethiopia": ["UI Issues", "Transaction Speed"],
    "Bank of Abyssinia": ["Login Errors", "App Crashes"],
    "Dashen Bank": ["Feature Requests", "Customer Support"]
}
df["themes"] = df["bank"].map(lambda x: themes.get(x, []))

# Save results, including the bank column
df[["review_id", "review", "rating", "date", "bank", "source", "sentiment_label", "sentiment_score", "keywords", "themes"]].to_csv(
    "data/sentiment_results.csv", index=False
)
print("Saved sentiment analysis results to data/sentiment_results.csv")