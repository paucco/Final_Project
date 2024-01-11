# Final Project
## Prediction of pollution in the center of Barcelona (Eixample) using Machine Learning in Python
***
This repository belongs to the final project of the Data Science course at IT Academy (Barcelona Activa). The main objective of the project is to predict the future pollution in the city center of Barcelona if no environmental measures or policies are implemented. To achieve this, knowledge in data analysis and data science acquired during the course has been applied.

All the steps followed in the project are explained in the repository; one simply needs to follow the provided order.

## Abstract
***
Urban pollution represents one of the most pressing environmental challenges today. As cities grow and develop, uncontrolled emissions of atmospheric pollutants become a threat to public health and the environment. Vehicles, industry, and other anthropogenic sources release contaminant particles such as nitrogen dioxide (NO2) and sulfur dioxide (SO2), as well as volatile organic compounds.

The final project of the IT Academy Data Science course focuses on predicting the future concentration of pollutants in the center of Barcelona if current levels are maintained. To achieve this, a dataset covering the concentration of various pollutants (CO, NO, NO2, PM10 and SO2) in Barcelona from 2018 to 2020 will be used. In addition to machine learning techniques, such as data splitting and supervised machine learning algorithms, an exploratory data analysis (EDA) will be conducted to understand the distribution and trends of pollutants over time. The implementation of the selected model and user data input will be made accessible through an interface developed using the Streamlit library. This will enable an intuitive and effective interaction, simplifying the utilization of the model.

With this approach, the project aims to demonstrate the utility of data-driven solutions, the use of machine learning for environmental issues, raise awareness about the need to improve air quality in cities, and motivate initiatives that promote environmental quality improvement in Barcelona.

## Overall Objective
***
Predict, through machine learning, the concentration of pollutants that would occur in the future in the center of Barcelona if current pollution levels are maintained.
### Specific Objectives
- Conduct an exploratory data analysis to understand the evolution of pollutant concentrations in Barcelona.
- Implement machine learning algorithms to model the relationship between variables and forecast future pollutant concentrations, evaluating the effectiveness of the models with relevant metrics.
- Develop predictive models with Python to support informed decision-making on environmental issues.
- Create an interface using the Streamlit library to provide users with a user-friendly experience for using the selected pollution prediction model.

## Dataset
***
The project is based on a dataset obtained from the Generalitat de Catalunya, specifically from the Dades Obertes (Open Data) department. This dataset covers records of various air pollutants in the city of Barcelona, more specifically from the monitoring station in l'Eixample, during the period from 2018 to 2023. The data was extracted from the website (20/12/2023): https://analisi.transparenciacatalunya.cat/en/Medi-Ambient/Qualitat-de-l-aire-als-punts-de-mesurament-manuals/qg74-87s9/about_data

## Methodology
***
In this project, the acquired knowledge from the course will be autonomously applied, focusing on two fundamental phases: data analysis and data science (application of machine learning algorithms).

In the initial stage of data analysis, the following libraries will be utilized: 

- NumPy
- Pandas
- Matplotlib
- Seaborn.

Techniques such as graphical visualizations and hypothesis testing will be employed. In the second phase, machine learning algorithms will be implemented:

- ML techniques such as data splitting (Train-Test), hyperparameter tuning (Grid Search CV), or comparisons (Cross-Validation).
- Different machine learning models (Linear Regression, K-Neighbors Regressor, Random Forest Regressor, among others).
- Analysis metrics to assess model effectiveness: R2 and MSE.
  
In the final phase, code will be developed using the Streamlit library to create a web page with the chosen model for prediction.
