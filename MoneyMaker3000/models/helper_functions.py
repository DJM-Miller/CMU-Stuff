from pandas import DataFrame
from pandas import concat
from sklearn.metrics import mean_absolute_error
from numpy import asarray
from xgboost import XGBRegressor



def get_set_sma(data):
    """
    Get Simple Moving Average for different ranges
    Input: 
        data: training data with adj_close still included
    Output:
        data with additional SMA features
    """

    data['sma_7'] = data['Adj Close'].rolling(window =7, center=False).mean()
    #data['sma_7'].fillna(data['sma_7'][6], inplace=True)
    data['sma_30'] = data['Adj Close'].rolling(window =30, center=False).mean()
    #data['sma_30'].fillna(data['sma_30'][29], inplace=True)
    data['sma_50'] = data['Adj Close'].rolling(window =50, center=False).mean()
    #data['sma_50'].fillna(data['sma_50'][49], inplace=True)
    #data['sma_100'] = data['Adj Close'].rolling(window =100, center=False).mean()
    #data['sma_100'].fillna(data['sma_100'][99], inplace=True)





#Function below was inspired by functions from website below
#https://machinelearningmastery.com/convert-time-series-supervised-learning-problem-python/
def create_lags(data, n_in=1, n_out=1, dropnan=True):
	"""
	create lag features for supervised learning
	Arguments:
		data: data frame you are using
		n_in: lag observations for input (train).
		n_out: lag observations as output (test).
		dropnan: drop rows with NaN values.
	Returns:
		DataFrame ready for supervised learning.
	"""
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg



# split a univariate dataset into train/test sets
def train_test_split(data, n_test):
 return data[:-n_test, :], data[-n_test:, :]

# fit an xgboost model and make a one step prediction
def xgboost_forecast(train, testX):
 # transform list into array
 train = asarray(train)
 # split into input and output columns
 trainX, trainy = train[:, :-1], train[:, -1]
 # fit model
 model = XGBRegressor(objective='reg:squarederror', n_estimators=1000)
 model.fit(trainX, trainy)
 # make a one-step prediction
 yhat = model.predict(asarray([testX]))
 return yhat[0]

#https://machinelearningmastery.com/xgboost-for-time-series-forecasting/
# walk-forward validation for univariate data
def walk_forward_validation(data, n_test):
	predictions = list()
	# split dataset
	train, test = train_test_split(data, n_test)
	# seed history with training dataset
	history = [x for x in train]
	# step over each time-step in the test set
	for i in range(len(test)):
		# split test row into input and output columns
		testX, testy = test[i, :-1], test[i, -1]
		# fit model on history and make a prediction
		yhat = xgboost_forecast(history, testX)
		# store forecast in list of predictions
		predictions.append(yhat)
		# add actual sample to history for the next loop
		history.append(test[i])
		#print('expected=%.1f, predicted=%.1f' % (testy, yhat))
	# estimate prediction error
	error = mean_absolute_error(test[:, -1], predictions)
	return error, test[:, -1], predictions

#Unfinished
def walk_forward_prediction(data, n_test):
	predictions = list()
	# split dataset
	train, test = train_test_split(data, n_test)
	# seed history with training dataset
	history = [x for x in train]
	# step over each time-step in the test set
	for i in range(len(test)):
		# split test row into input and output columns
		testX, testy = test[i, :-1], test[i, -1]
		# fit model on history and make a prediction
		yhat = xgboost_forecast(history, testX)
		# store forecast in list of predictions
		predictions.append(yhat)
		# add actual observation to history for the next loop
		print(test[i])
		history.append(test[i])
		# summarize progress
		print('expected=%.1f, predicted=%.1f' % (testy, yhat))
	# estimate prediction error
	error = mean_absolute_error(test[:, -1], predictions)
	return error, test[:, -1], predictions