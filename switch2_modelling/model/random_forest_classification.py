from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import GridSearchCV
import joblib
import os


# Train a classifier version for integer review scores.
def train_random_forest_classifier(X_train, y_train):
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }

    y_train = y_train.values.ravel().astype(int)

    clf = RandomForestClassifier(random_state=42, class_weight="balanced")
    grid_search = GridSearchCV(clf, param_grid, cv=3, scoring="accuracy")
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("Best Random Forest Classifier parameters found:", grid_search.best_params_)

    model_dir = os.path.join(os.path.dirname(__file__), "saved_models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_model, os.path.join(model_dir, "best_random_forest_classifier_model.joblib"))

    return best_model


# Evaluate classifier performance on exact score prediction.
def evaluate_random_forest_classifier(model, X_test, y_test):
    y_test = y_test.values.ravel().astype(int)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro")

    print(f"Classifier Accuracy: {accuracy}")
    print(f"Classifier Macro F1: {macro_f1}")

    return {
        "accuracy": accuracy,
        "macro_f1": macro_f1
    }
