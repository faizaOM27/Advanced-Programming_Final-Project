from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import joblib
import os


# Training function that also automatically looks for the best set of parameters.
def train_gradient_boosting(X_train, y_train, scoring="neg_mean_absolute_error"):
    # Parameter grid to tune Gradient Boosting for this dataset size.
    param_grid = {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [2, 3, 4],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "subsample": [0.8, 1.0]
    }

    # Flattening the target variable for compatibility with the model, at first it gave multiple warning about the shape, this ensures it doesn't.
    y_train = y_train.values.ravel()

    gb = GradientBoostingRegressor(random_state=42)

    # Use MAE by default because review scores are integer-like labels.
    grid_search = GridSearchCV(gb, param_grid, cv=3, scoring=scoring)
    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_

    print("Best Gradient Boosting parameters found:", grid_search.best_params_)
    print("Scoring used:", scoring)

    # Saving the best model to a file in the new saved_models folder, so that it can be loaded later without needing to retrain it.
    model_dir = os.path.join(os.path.dirname(__file__), "saved_models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_model, os.path.join(model_dir, "best_gradient_boosting_model.joblib"))

    return best_model


# Function to evaluate the Gradient Boosting model.
def evaluate_gradient_boosting_model(model, X_test, y_test):

    # Flattening the target variable for compatibility with the model, at first it gave multiple warning about the shape, this ensures it doesn't.
    y_test = y_test.values.ravel()

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)


    # Integer-aware evaluation for score prediction tasks.
    y_min = int(np.min(y_test))
    y_max = int(np.max(y_test))
    y_pred_int = np.clip(np.rint(y_pred), y_min, y_max).astype(int)
    y_test_int = y_test.astype(int)

    exact_accuracy = (y_test_int == y_pred_int).mean()
    int_mae = mean_absolute_error(y_test_int, y_pred_int)

    print(f"Gradient Boosting Mean Squared Error: {mse}")
    print(f"Gradient Boosting Mean Absolute Error: {mae}")
    print(f"Gradient Boosting R^2 Score: {r2}")
    print(f"Gradient Boosting Integer Exact Accuracy: {exact_accuracy}")
    print(f"Gradient Boosting Integer MAE: {int_mae}")

    return {
        "mse": mse,
        "mae": mae,
        "r2": r2,
        "integer_exact_accuracy": exact_accuracy,
        "integer_mae": int_mae
    }
