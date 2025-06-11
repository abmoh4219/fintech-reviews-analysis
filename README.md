# Fintech Reviews Analysis

## Overview
This repository contains code and deliverables for the **Week 2 Challenge** of the **Tenx Platform**, focusing on analyzing customer satisfaction for Ethiopian bank mobile apps (CBE, BOA, Dashen). The project involves scraping Google Play Store reviews, performing sentiment and thematic analysis, and generating actionable insights.

---

## Tasks

### Task 1: Data Collection and Preprocessing
**Objective**: Scrape 400+ reviews per bank (1,200 total) from Google Play Store, preprocess the data, and save it as a CSV file.

**Tools**: 
- `google-play-scraper` for scraping
- `pandas` for preprocessing

**Methodology**:
1. Scrape reviews, ratings, dates, and app names using `google-play-scraper`.
2. Remove duplicates and normalize dates to the format `YYYY-MM-DD`.
3. Save the data as a CSV file with the following columns:
   - `review`
   - `rating`
   - `date`
   - `bank`
   - `source`

---

### Next Steps
1. **Task 2**: Perform sentiment analysis and thematic analysis.
2. **Task 3**: Store the data in an Oracle database.
3. **Task 4**: Generate insights and visualizations.

---

## Repository Structure
```
├── data/                  # Contains raw and processed data files
│   ├── bank_reviews.csv   # Preprocessed review data
│   ├── sentiment_results.csv # Sentiment analysis results
├── src/                   # Source code for data processing and analysis
│   ├── create_tables.sql  # SQL script for creating database tables
│   ├── database_migration.py # Script for migrating data to Oracle DB
│   ├── result.py          # Script for analyzing sentiment results
│   ├── sentiment_analysis.py # Script for sentiment analysis
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore             # Excludes unnecessary files
```

---

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/fintech-reviews-analysis.git
   cd fintech-reviews-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the scripts:
   - **Data Collection**: `python src/scrape_review.py`
   - **Database Migration**: `python src/database_migration.py`
   - **Sentiment Analysis**: `python src/sentiment_analysis.py`
   - **Analyze Results**: `python src/result.py`

4. Create database tables:
   - Use the `create_tables.sql` script to set up the Oracle database:
     ```bash
     sqlplus system/<password> @src/create_tables.sql
     ```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or feedback, please contact [Your Name](mailto:abdelahmohammed0919@gmail.com).

