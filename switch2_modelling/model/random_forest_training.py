from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
import numpy as np
import joblib
import os

# Training function that also automatically looks for the best set of parameters.
def train_random_forest_regression(X_train, y_train, scoring="neg_mean_absolute_error"):
    # I defined a parameter grid, so that the model can be tuned to find the best parameters.
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    # Flattening the target variable for compatibility with the model, at first it gave multiple warning about the shape, this ensures it doesn't.
    y_train = y_train.values.ravel()  

    # Creating the random forest regression model
    rf = RandomForestRegressor(random_state=42)

    # Here the grid search is used, I set cv = 3 because the model has about 120 data lines,
    # so I think 3 folds should be enough to find the best set of parameters.
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring=scoring)
    grid_search.fit(X_train, y_train)

    # Getting the best model
    best_model = grid_search.best_estimator_

    print("Best parameters found:", grid_search.best_params_)
    print("Scoring used:", scoring)

    # Saving the best model to a file in the new saved_models folder, so that it can be loaded later without needing to retrain it.
    model_dir = os.path.join(os.path.dirname(__file__), "saved_models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_model, os.path.join(model_dir, "best_random_forest_model.joblib"))

    return best_model

# A function to evaluate the model. 
def evaluate_random_forest_regression(model, X_test, y_test):

    # Flattening the target variable for compatibility with the model, at first it gave multiple warning about the shape, this ensures it doesn't.
    y_test = y_test.values.ravel()

    # Making predictions
    y_pred = model.predict(X_test)

    # Evaluating the raw regression predictions.
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

    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")
    print(f"R^2 Score: {r2}")
    print(f"Integer Exact Accuracy: {exact_accuracy}")
    print(f"Integer MAE: {int_mae}")

    return {
        "mse": mse,
        "mae": mae,
        "r2": r2,
        "integer_exact_accuracy": exact_accuracy,
        "integer_mae": int_mae
    }