import pandas as pd
df = pd.read_csv("data/bank_reviews.csv", encoding='utf-8')
max_length = df['review'].str.len().max()
sample_review = df.loc[df['review'].str.len() == max_length, 'review'].iloc[0]
print(f"Maximum review length: {max_length}")
print(f"Sample longest review: {sample_review}")