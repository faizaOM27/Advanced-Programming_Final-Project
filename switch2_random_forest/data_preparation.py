from pandas import read_csv
from sklearn.model_selection import train_test_split

# A function to prepare the data by splitting it.
def data_preparation(dataset_path, target_column):
    # Loading the dataset
    dataset = read_csv(dataset_path)

    # Separating the features and target variable
    X = dataset.drop(target_column, axis=1)
    y = dataset[target_column]

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test