import pandas as pd
df = pd.read_csv("data/sentiment_results.csv")
for bank in df["bank"].unique():
    bank_df = df[df["bank"] == bank]
    total = len(bank_df)
    pos = len(bank_df[bank_df["sentiment_label"] == "positive"]) / total * 100
    neg = len(bank_df[bank_df["sentiment_label"] == "negative"]) / total * 100
    neu = len(bank_df[bank_df["sentiment_label"] == "neutral"]) / total * 100
    print(f"{bank}: {pos:.1f}% positive, {neg:.1f}% negative, {neu:.1f}% neutral")