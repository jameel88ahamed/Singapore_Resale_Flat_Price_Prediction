# Singapore_Resale_Flat_Price_Prediction

## Introduction
The resale flat market in Singapore is highly competitive, and it can be challenging to accurately estimate the resale value of a flat. There are many factors that can affect resale prices, such as location, flat type, floor area, and lease duration. A predictive model can help to overcome these challenges by providing users with an estimated resale price based on these factors. By considering historical sales data and current market trends, the model enhances the accuracy of property valuations in Singapore's dynamic real estate market.

## Problem Statement
The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.

## Required Libraries:
- Streamlit : To Create Graphical user Interface and build web application.
- Pandas : To Clean and maipulate the data.
- NumPy: A library for numerical computations in Python.
- Matplotlib: A plotting library for creating visualizations.
- Seaborn: A data visualization library built on top of Matplotlib.
- Pickle: Library used for saving the model and use whenever required.
- Scikit-learn: A machine learning library that provides various regression and classification algorithms & Evaluation Metrices.

## Workflow:
1. Data Collection and Preprocessing:
   - Collecting a dataset of resale flat transactions from the Singapore Housing and Development Board (HDB) for the years 1990 to Till Date.
   - Applying preprocessing techniques like removing null values, imputing missing data, removing duplicates and outliers, and handling skewness to clean and structure the data for machine learning.
2. Feature Engineering:
   - Extracting relevant features from the dataset, including town, flat type, storey range, floor area, flat model, remaining lease period, and lease commence date.
   - Creating any additional features that may enhance prediction accuracy.
3. Model Selection and Training:
   - Choosing an appropriate machine learning model for regression (e.g., linear regression, decision trees, or random forests).
   - Training the model on the historical data, using a portion of the dataset for training.
4. Model Evaluation: Evaluating the model's predictive performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), or Root Mean Squared Error (RMSE) and R2 Score.
5. Streamlit Web Application:
   - Developing a user-friendly web application using Streamlit that allows users to input details of a flat (town, flat type, storey range, etc.,).
   - Utilizing the trained machine learning model to predict the resale price based on user inputs.
6. Deployment on Render: Deploying the Streamlit application on the Render platform to make it accessible to users over the internet.
7. Testing and Validation: Thoroughly testing the deployed application to ensure it functions correctly and provides accurate predictions.

## Learning Outcomes:
- Experienced in Python and its data analysis libraries, including Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit.
- Acquiring expertise in data preprocessing techniques, encompassing handling missing values, imputing missing values, outlier detection, and converting data into correct data types format to optimize data for machine learning modeling.
- Understanding and visualizing the data distribution using EDA techniques such as boxplots, distribution plot, density plot, & histograms.
- Learned advanced machine learning techniques including regression and random forest for predictive modeling, alongside optimizing models through evaluation metrics like MSE, MAE, RMSE & R2-score.
- Experienced in feature engineering techniques to create new informative representations of the data and generate additional features for improved accuracy.
- Developing a web application using the Streamlit module to showcase the machine learning models and make predictions on new data.
- Deploying the model on the Render platform to help buyers and sellers accurately predict the resale price based on their requirements.

## Conclusion
This project benefits both potential buyers and sellers in the Singapore housing market by providing buyers with tools to estimate resale prices for informed decision-making, giving sellers insights into their flat's potential market value, and demonstrating the practical application of machine learning in real estate and web development.
