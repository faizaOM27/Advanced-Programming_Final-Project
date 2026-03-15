import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os


def load_dataset(csv_path):
    """Load the scraped review dataset."""
    df = pd.read_csv(csv_path)

    df = df.dropna(subset=["review_text", "score"])

    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df = df.dropna(subset=["score"])

    return df


def create_vectorizer():
    """Create TF-IDF vectorizer."""

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        max_features=3000,
        ngram_range=(1, 2)
    )

    return vectorizer


def vectorize_reviews(texts, vectorizer):
    """Convert review text into TF-IDF vectors."""
    X = vectorizer.fit_transform(texts)
    return X

# New version, changed the output files from pickle to csv, which is easier to handle for the random forest regression model.
def save_outputs(X, y, vectorizer, output_dir="data"):
    """Save features and vectorizer as DataFrame."""

    os.makedirs(output_dir, exist_ok=True)

    # Converting the vectorized reviews to a DataFrame.
    X_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

    # Saving the dataframe as CSV.
    X_df.to_csv(f"{output_dir}/X_features.csv", index=False)

    # Saving the score as CSV.
    y_df = pd.DataFrame(y, columns=["score"])
    y_df.to_csv(f"{output_dir}/y_scores.csv", index=False)

    # Saving the vectorizer as pickle, which can be loaded later if needed.
    with open(f"{output_dir}/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
