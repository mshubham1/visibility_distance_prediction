
# Visibility Distance Prediction

To build a regression model to predict the visibility distance based on the given different climatic indicators in the training data. 
Visibility affects all forms of traffic: roads, sailing, and aviation. Visibility prediction is meaningful in guiding production and life.

## Table Content ✏️
* Demo
* Overview
* Dataset
* Installation
* Deployment
* Documentation
* Directory Tree
* Technology Used
* Bug/Feature Request
* Future scope of project
## Demo

![ezgif com-gif-maker](https://user-images.githubusercontent.com/47842305/140636425-408f65bd-e42c-41dc-a2ca-159e3ee3e668.gif)

Heroku:- https://visibility_distance_prediction.herokuapp.com/

## Overview  📜
The application is a web app which is developed in Flask Framework.
* Data Exploration - Using pandas,numpy,matplotlib and seaborn.
* Data Visulization- Insights obtained through graph about dependent and independent variable.
* Feature Engineering - Drop the column with higher correlation and perform StandardScaler to scale the data.
* Model Training - Trained the model with different regressor algo and obtained the DecisionTreeRegressor with best score.
* Deployment - Biuld the webpage through Streamlit Library and deployed on heroku app.

## Dataset  
Dataset available in IBM : https://developer.ibm.com/exchanges/data/all/jfk-weather-data/

The NOAA JFK dataset contains 114,546 hourly observations of various local climatological variables (including visibility, temperature, wind speed and direction, humidity, dew point, and pressure). The data was collected by a NOAA weather station located at the John F. Kennedy International Airport in Queens, New York.
## Installations  🗄️
The Code is written in Python 3.8 If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
```bash
  pip install -r requirements.txt
```
## Deployment
![image](https://user-images.githubusercontent.com/47842305/140636459-9a17b723-7da8-45f9-afeb-0c22f78223f4.png)

## Database 
![Screenshot (33)](https://user-images.githubusercontent.com/47842305/140636439-2d0e4a19-f3ed-44c5-8d2a-b83a39bf7f88.png)

## Tree Structure
```javascript
├── database
│   ├──logger.py
├── log_file
│   ├── db_operation.txt
│   ├── Model_tarining.txt
├── models
│   ├── database.html
│   ├── index.html
├── templates
│   ├── model_train
│   ├── index.html
├── EDA.ipynb
├── Procfile.txt
├── jkf_weather_cleaned.csv
├── app1.py
├── requirements.txt
├── README.md

```


## Technologies Used

* Python
* FrontEnd: HTML & CSS
* Backend: Flask 
* Deployment : AWS, Heroku

![image](https://user-images.githubusercontent.com/47842305/140639851-383d14d8-aff7-4cd0-ae5d-68a456f2f317.png)
![image](https://user-images.githubusercontent.com/47842305/140639859-bc1aa162-84c8-488f-b284-34db2b6fee2b.png)
![image](https://user-images.githubusercontent.com/47842305/140639874-6c2d32d4-2abc-4f1a-8631-e2c0dd546d66.png)


## Contributers
You can feel free to reach out me at shubhammourya2014@gmail.com

@Shubham Mourya
