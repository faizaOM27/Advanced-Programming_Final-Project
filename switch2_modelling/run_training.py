import os
import sys
from pathlib import Path

# Fix imports for model subfolder
script_dir = Path(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(script_dir))

import model
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split

def get_data_paths():
    """Get absolute paths to vectorization data"""
    script_dir = Path(os.path.dirname(os.path.abspath(__file__)))  
    project_root = script_dir.parent 
    vectorization_data = project_root / "switch2_vectorization" / "data"
    
    x_path = vectorization_data / "X_features.csv"
    y_path = vectorization_data / "y_scores.csv"
    
    return x_path, y_path

def main():
    
    # Load data
    print("Loading training data...")
    x_path, y_path = get_data_paths()
    
    X_train, X_test, y_train, y_test = model.data_preparation(str(x_path), str(y_path))
    
    print(f"X_train: {X_train.shape}")
    print(f"X_test: {X_test.shape}")
    
    # Train & evaluate ALL models 
    print("Training Random Forest Regression...")
    rf_reg_model = model.train_random_forest_regression(X_train, y_train)
    rf_reg_metrics = model.evaluate_random_forest_regression(rf_reg_model, X_test, y_test)
    
    print("\nTraining Gradient Boosting...")
    gb_reg_model = model.train_gradient_boosting(X_train, y_train)
    gb_reg_metrics = model.evaluate_gradient_boosting_model(gb_reg_model, X_test, y_test)
    
    print("\nTraining Random Forest Classifier...")
    rf_clf_model = model.train_random_forest_classifier(X_train, y_train)
    rf_clf_metrics = model.evaluate_random_forest_classifier(rf_clf_model, X_test, y_test)
    
    print("\nTraining complete! Models saved to model/saved_models/")
    
    # Test prediction with random forest regression model
    print("\nTesting predictions...")
    predictions = rf_reg_model.predict(X_test)
    df_results = pd.DataFrame({
        "Predictions": predictions,
        "Actual": y_test["score"].to_numpy()
    })
    print("\nSample predictions:")
    print(df_results.head(10))

if __name__ == "__main__":
    main()
