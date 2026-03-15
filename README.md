# Advanced-Programming---Final-Project

The main goal of this project is to scrape switch 2 reviews from NintendoLife and try to train a model on it to predict what score
should be assigned to the review. We do this by vectorizing the review text and using this vectorization and existing scores to train
several different models. Right now the models available for training are a random forest regressor, random forest classifier and a 
gradient boosting model. 

For running this project, please create a new environment and install the depencies as listed in the requirements.txt
Please note that some paths to the files might have to be changed accordingly, dependending on where you run the code.

This repo consists of 3 folders, one for each step in the process. We will go over them in this file.

1. switch2_scraper

2. switch2_vectorization

3. switch2_modelling
    - Contains a module called 'model', after importing model you can use:
        - data_preparation; to split the data in train and test data.

        - train_gradient_boosting; to train a gradient boosting model.
        - evaluate_gradient_boosting_model; to evaluate the trained gradient boosting model.

        - train_random_forest_classifier; to train a random forest classifier.
        - evaluate_random_forest_classifier; to evaluate a random forest classifier.

        - train_random_forest_regression; to train a random forest regressior.
        - evaluate_random_forest_regression; to evaluate a random forest regresssior.

    - Contains a notebook in which you can run and test above mentioned functions to train the models.

