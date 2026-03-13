from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import GridSearchCV

# Training function that also automatically looks for the best set of parameters.
def train_random_forest(X_train, y_train):
    # I defined a parameter grid, so that the model can be tuned to find the best parameters.
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10]
    }

    # Creating the random forest regression model
    rf = RandomForestRegressor(random_state=42)

    # Here the grid search is used, I set cv = 3 because the model has about 120 data lines,
    # so I think 3 folds should be enough to find the best set of parameters.
    grid_search = GridSearchCV(rf, param_grid, cv=3, scoring="neg_mean_squared_error")
    grid_search.fit(X_train, y_train)

    # Getting the best model
    best_model = grid_search.best_estimator_

    print("Best parameters found:", grid_search.best_params_)

    return best_model

# A function to evaluate the model. 
def evaluate_model(model, X_test, y_test):
    # Making predictions
    y_pred = model.predict(X_test)

    # Evaluating the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")
    print(f"Accuracy: {accuracy}")