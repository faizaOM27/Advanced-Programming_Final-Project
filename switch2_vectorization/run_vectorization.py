from vectorizer.tfidf_vectorizer import (
    load_dataset,
    create_vectorizer,
    vectorize_reviews,
    save_outputs
)


def main():

    print("Loading dataset...")
    df = load_dataset("switch2_reviews.csv")

    texts = df["review_text"]
    scores = df["score"]

    print("Creating TF-IDF vectorizer...")
    vectorizer = create_vectorizer()

    print("Vectorizing reviews...")
    X = vectorize_reviews(texts, vectorizer)

    print("Saving outputs...")
    save_outputs(X, scores, vectorizer)

    print("Vectorization complete.")
    print("Samples:", X.shape[0])
    print("Features:", X.shape[1])


if __name__ == "__main__":
    main()