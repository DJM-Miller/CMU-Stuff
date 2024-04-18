# MoneyMaker3000
## Final Project for Prof.Basnet's Python Machine Learning by Darrin Miller and Riley Primeau. 

### The Money Maker 3000 is a collection of machine learning models aimed at stock price forcasting. Two main types of models exist in this repo, Regression models forcasting future values related to the stock and Classification models aimed at classifying whether tomorrows stock will show an increase based on stock data as well as news sentiment related to that company.These models are meant to an explorations of the possiblility of using machine learning models to gather information that could then be used to develop successful trading strategies.

| Name | Value |
|:---|:---|
| Model | adjCloseForcaster |
| Description | Xgboost regression model to predict adjusted Close |
| Status | working |
| Location | https://github.com/DJM-Miller/MoneyMaker3000/blob/main/models/adjCloseForcaster.ipynb |
|:---|:---|
| Model | dailyRetForcaster |
| Description | Xgboost regression model to predict daily return based on each days adjusted close |
| Status | working |
| Location | https://github.com/DJM-Miller/MoneyMaker3000/blob/main/models/dailyRetForcaster.ipynb |
|:---|:---|
| Model | classification |
| Description | Xgboost classification model using stock data and new sentiment to predict whether future stock value increases |
| Status | proof of concept |
| Note | Struggles acquiring up to date daily news sentiment data has prevented future predictions |
| Location | https://github.com/DJM-Miller/MoneyMaker3000/blob/main/models/classification.ipynb |