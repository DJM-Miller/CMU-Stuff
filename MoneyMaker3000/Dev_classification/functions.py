import pandas as pd
from pandas import DataFrame
import requests
import json
import datetime
import openai
import time
from pandas_datareader import data as pdr
from datetime import date, timedelta
import yfinance as yf

def combine_dataframes(stock_data: DataFrame, sentiment: DataFrame) -> DataFrame:
	# ensure indices are of the same type 
	sentiment.index = pd.to_datetime(sentiment.index)

	# create sentiment column in stock dataframe
	stock_data['Sentiment'] = pd.Series(dtype='float64')

	# insert sentiment at a date if it exists
	for date in stock_data.index:
		if date in sentiment.index:
			stock_data.loc[date, 'Sentiment'] = sentiment.loc[date, 'normalized']

	# print(type(stock_data.index))
	# print(type(sentiment.index))

	return stock_data

def create_increase_feature(stock_data:DataFrame, column:str) -> DataFrame:
	stock_data['Increase'] = pd.Series(dtype='bool')
	for i in range(len(stock_data) - 1):
		if stock_data.iloc[i+1][column] > stock_data.iloc[i][column]:
			ith_date = stock_data.index[stock_data.index.isin([stock_data.index[i+1]])][0]
			# print(ith_date)
			stock_data.at[ith_date, 'Increase'] = 1
		else:
			ith_date = stock_data.index[stock_data.index.isin([stock_data.index[i+1]])][0]
			stock_data.at[ith_date, 'Increase'] = 0
	return stock_data

def create_daily_return(stock_data:DataFrame) -> DataFrame:
	stock_data.loc[:, 'daily_return'] = (stock_data['Close'] - stock_data['Open'])
	return stock_data

def create_top_feature_ratios(stock_data:DataFrame) -> DataFrame:
	stock_data.loc[:, 'Sentiment/volume'] = (stock_data['Sentiment']/stock_data['Volume'])
	stock_data.loc[:, 'dr/volume'] = (stock_data['daily_return']/stock_data['Volume'])
	return stock_data

def create_lag_featues(stock_data:DataFrame) -> DataFrame:
	stock_data = create_lag_features(stock_data, 'Open', lag=7)
	stock_data = create_lag_features(stock_data, 'Sentiment', lag=7)
	stock_data = create_lag_features(stock_data, 'Volume', lag=7)
	stock_data = create_lag_features(stock_data, 'daily_return', lag=7)
	return stock_data

def create_lag_features(df, column_name, lag=1):
    """
    Creates lag features for a given column of a pandas DataFrame.
    
    Parameters
    ----------
    df : pandas DataFrame
        The DataFrame containing the column to create lag features for.
    column_name : str
        The name of the column to create lag features for.
    lag : int, default 1
        The number of lags to create.
    
    Returns
    -------
    pandas DataFrame
        The DataFrame with the original column and its lag features.
    """
    lag_column_names = [f"{column_name}_lag{i}" for i in range(1, lag+1)]
    lag_columns = [df[column_name].shift(i) for i in range(1, lag+1)]
    df_with_lag = df.assign(**dict(zip(lag_column_names, lag_columns)))
    return df_with_lag

def standardize(stock_data:DataFrame) -> DataFrame:
	for column in stock_data.columns:
		min_value = stock_data[column].min()
		max_value = stock_data[column].max()
		# apply the scaling formula to each value in the column
		stock_data[column] = stock_data[column].apply(lambda x: (x - min_value) / (max_value - min_value) * 100)

	return stock_data	

def get_data_for(ticker:str) -> DataFrame:
	"""Does the heavy lifting for getting the correct data for the model

	Args:
		ticker (str): Ticker symbol

	Returns:
		DataFrame: returns a DataFrame the model can predict with
	"""	 
	# get today's date
	today = datetime.date.today()

	# get the date from one month ago
	one_month_ago = today - datetime.timedelta(days=30)

	# format the date in year-month-day format
	date_str = one_month_ago.strftime("%Y-%m-%d")

	# set up the API endpoint URL
	url = f"https://newsapi.org/v2/everything?q=google&from={date_str}&to={today}&sortBy=popularity&apiKey=2f014b5262fc406e8b9288e8d456284b"

	# make the API request
	response = requests.get(url)

	# loads response as json in results
	results = json.loads(response.text)

	# create lists
	articles = []
	dates = []

	# fill lists
	for article in results["articles"]:
		articles.append(article['title'])
		dates.append(article['publishedAt'])

	# ensure dates are in correct format
	formatted_dates = []

	for date in dates:
		date = date[:10] # remove unwanted last 15 characters 
		formatted_dates.append(date)

	formatted_dates
	date_objs = [datetime.datetime.strptime(date_str, '%Y-%m-%d') for date_str in formatted_dates]
	date_objs

	# create articles dataframe
	df = pd.DataFrame(list(zip(articles, date_objs)), columns=['Articles', 'Dates'])

	# remove unrealted articles from df
	# and the list of words is stored in a variable called "keywords"
	keywords = ['Google', 'Alphabet', 'Search', 'Advertising', 'Android', 'YouTube', 'Chrome', 'Maps', 'Gmail', 'Pixel', 'Assistant', 'Cloud', 'Drive', 'Play', 'Nexus', 'Chromebook']

	# filter the rows that dont contain at least one of the keywords
	df = df[df['Articles'].str.contains('|'.join(keywords))]

	# api key for getting sentiment from chat
	#open ai api call removed for safety

	# gets chat to rank the articles
	count = 0
	start_time = time.time()
	for index, row in df.iterrows():
		if count < 60: 
			count += 1
			prompt = f"On a scale of 0-100, how positive would you rate this headline for the related company? Be specific with your scale to the ones place. Headline: {row['Articles']}"

			response = openai.Completion.create(
			engine="text-davinci-001",
			prompt=prompt,
			max_tokens=1024,
			n=1,
			stop=None,
			temperature=0.7,
			)
			
			message = response.choices[0].text
			df.loc[index, 'Sentiment'] = message
			
		else: 
			end_time = time.time()
			count = 0
			elapsed_time = end_time - start_time
			print(elapsed_time)
			time.sleep(60 - elapsed_time)
			start_time = time.time()

	# cleans the output
	df['Sentiment'] = df['Sentiment'].str.replace('\n', '')
	df['Sentiment'] = df['Sentiment'].apply(lambda x: ''.join(filter(str.isdigit, str(x))))

	# Get Stock info from Yahoo Finance
	yf.pdr_override()
	ticker_symbol = ticker
	data = pdr.get_data_yahoo(ticker_symbol, start=one_month_ago, end=today)


	# makes sure indices are of the same type in order to merge
	df.set_index('Dates', inplace=True) # set "date" column as index
	df.index = pd.to_datetime(df.index)

	# merges data into result df
	result = data.merge(df, left_index=True, right_index=True)

	# clean and format for the model
	result.drop('Articles', inplace=True, axis=1)
	result = result[result['Sentiment'] != ''] # cant convert '' to int
	result['Sentiment'] = result['Sentiment'].astype('int')
	result = result[result['Sentiment'] <= int(100)] # make sure sentiment values are reasonable 
	# check if index values are unique
	if not result.index.is_unique:
		# drop any duplicate rows
		result = result[~result.index.duplicated(keep='first')]

	# add additional features
	result = create_daily_return(result)
	result = create_top_feature_ratios(result)
	result = create_lag_featues(result)

	# drop unhelpful ones
	result.drop(['Low', 'Open_lag2', 'Open_lag3', 'Open_lag7', 'High', 'Close', 'Open_lag5', 'Open_lag4', 'Sentiment_lag2', 'Volume_lag7', 'Open', 'Open_lag1', 'Open_lag6'], axis=1, inplace=True)

	# grab last row
	final_data = result.iloc[-1]
	final_data = final_data.to_frame()
	final_data = final_data.transpose()
	final_data = final_data.astype(float)

	return final_data


