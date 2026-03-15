from pandas import read_csv
from sklearn.model_selection import train_test_split

# A function to prepare the data by splitting it.
def data_preparation(x_path, y_path):

    # Separating the features and target variable.
    X = read_csv(x_path)
    y = read_csv(y_path)

    # Splitting the data into training and testing sets.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test