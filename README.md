# Advanced-Programming---Final-Project

The main goal of this project is to scrape switch 2 reviews from NintendoLife and try to train a model on it to predict what score
should be assigned to the review. We do this by vectorizing the review text and using this vectorization and existing scores to train
several different models. Right now the models available for training are a random forest regressor, random forest classifier and a 
gradient boosting model. 

For running this project, please create a new environment and install the depencies as listed in the requirements.txt
Please note that some paths to the files might have to be changed accordingly, dependending on where you run the code, if you just run the functions like described below it should work.

This repo consists of 3 folders, one for each step in the process. We will go over them in this file.

1. switch2_scraper
    - Contains a module called 'scraper' and 'data', which is used to scrape raw text from the NintendoLife website and convert it into a dataframe.
    - After importing the model 'scraper' you can use:
        - NintendoLifeClient; to initialize HTTP client with rate limiting.
        - scrape_browse_page; to scrape Switch 2 games from the browse page.
        - scrape_review_links; to extract review URLs from game pages.
        - scrape_full_review; to extract scores and full multi-paragraph review text from review pages.
    - After importing the model 'data' you can use:
        - games_to_df; to convert game list ot pandas DataFrame.
        - reviews_to_df; to convert review list to DataFrame with game/review/score/text columns.
        - save_reviews; to export reviews to CSV
    - Contains main.py script that runs the full pipeline
    - The resulting files are used as input for the vectorizer
2. switch2_vectorization
    - Contains a module called 'vectorizer', which is used to convert the review text into numerical features
      using TF-IDF vectorization.
    - After importing the model you can use:
        - load_dataset; to load the scraped review dataset from the csv file and perform basic data cleaning.
     
        - create_vectorizer; to initialize the TF-IDF vectorizer with predefined parameters.
     
        - vectorize_reviews; to transform the review text into a TF-IDF feature matrix.
     
        - save_outputs; to store the generated feature matrix (X), review scores (y) and the trained vectorizer object in the data folder as csv files.
    
    - The resulting files are used as input for the modelling step in the project.
    - Contains a script that runs the full vectorization pipeline, starting from the scraped csv file and
      producing the feature matrix and saved objects required for the modelling stage.
3. switch2_modelling
    - Contains a module called 'model', after importing model you can use:
        - data_preparation; to split the data in train and test data.

        - train_gradient_boosting; to train a gradient boosting model.
        - evaluate_gradient_boosting_model; to evaluate the trained gradient boosting model.

        - train_random_forest_classifier; to train a random forest classifier.
        - evaluate_random_forest_classifier; to evaluate a random forest classifier.

        - train_random_forest_regression; to train a random forest regressior.
        - evaluate_random_forest_regression; to evaluate a random forest regresssior.

    - Contains a py file with which you can run the training through 'main'.

