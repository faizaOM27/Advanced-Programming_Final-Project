import os
import sys

from vectorizer.tfidf_vectorizer import (
    load_dataset,
    create_vectorizer,
    vectorize_reviews,
    save_outputs
)

# script directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'vectorizer'))


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "switch2_reviews.csv")
    
    print("Loading dataset...")
    df = load_dataset(csv_path)

    texts = df["review_text"]
    scores = df["score"]

    print("Creating TF-IDF vectorizer...")
    vectorizer = create_vectorizer()

    print("Vectorizing reviews...")
    X = vectorize_reviews(texts, vectorizer)

    print("Saving outputs...")
    project_data_dir = os.path.join(os.path.dirname(__file__), "data")
    save_outputs(X, scores, vectorizer, output_dir=project_data_dir)

    print("Vectorization complete.")
    print("Samples:", X.shape[0])
    print("Features:", X.shape[1])


if __name__ == "__main__":
    main()