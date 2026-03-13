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


def save_outputs(X, y, vectorizer, output_dir="data"):
    """Save features and vectorizer."""

    os.makedirs(output_dir, exist_ok=True)

    with open(f"{output_dir}/X_features.pkl", "wb") as f:
        pickle.dump(X, f)

    with open(f"{output_dir}/y_scores.pkl", "wb") as f:
        pickle.dump(y, f)

    with open(f"{output_dir}/tfidf_vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)