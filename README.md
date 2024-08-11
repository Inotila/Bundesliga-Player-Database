# Top goal scorer prediction

For this project I have choosen data set: Football/Soccer | Bundesliga Player Database from  " https://www.kaggle.com/datasets/oles04/bundesliga-soccer-player ".

I will use this to predict the price of a football player based on their age. This could be useful for a club that whats to get a valution on a player they own or want to own based on their age.

## Algorithms for this problem:

### Linear Regression:
Which is suitable for predicting continuous values. It assumes that there is a linear relationship between the features and the target variable.  I have chosen as a baseline model to understand the linear relationships between the position of the player and the target variable the price of player.

### Random Forest Regressor:
Which is an ensemble method that combines multiple decision trees. And does a good job at handling non-linear relationships and interactions between features. This will is capture non-linear relationships and feature interactions.

### Gradient Boosting Regressor:
Which builds models sequentially to correct errors of previous models. It works well with a variety of datasets and provides good accuracy. And it has the ability to improve prediction accuracy through iterative learning.

# API for Player Price Prediction
To make the player price prediction model accessible and usable, I have developed a RESTful API using Flask. This API allows users to request predictions based on player age and receive the predicted price along with a confidence value for each model.

# API Endpoints
## POST /predict
### Description: 
This endpoint receives the age of a football player and returns predictions of the player’s price using the trained models. It also provides a confidence value associated with each prediction.

## Request Format:

URL: http://127.0.0.1:5000/predict
Method: POST
Headers:
    Content-Type: application/json

Body (Example):
{
  "age": 29
}

Response Format:

Content-Type: application/json

Body (Example):
{
  "random_forest": {
    "confidence": 0.85,
    "prediction": 12.34
  },
  "gradient_boosting": {
    "confidence": 0.90,
    "prediction": 11.56
  }
}

## How to Use the API
Run Jupyter Notebook -> player_price_prediciton.ipynb

Run the API Server, start it by running the following command:

python3 api.py

Make a POST Request: Using Postman or curl to send a POST request to the API endpoint. 

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"age": 29}'

# Bugs

The confidence value is too high and the data set I have used is a  little challenging to express as a probablity. 
More work will need to be done as this bug has not been fixed yet.

## Credits/Reference
This work is the original work of Inotila Nghaamwa, however resources from school material and other accedemice sources were used to supplement, for example the data is from www.kaggle.com

### Credits

Content - Inotila Nghaamwa and www.kaggle.com
Text-Written by Inotila Nghaamwa.