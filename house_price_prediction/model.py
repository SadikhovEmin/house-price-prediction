import bcolors as b
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import hvplot.pandas
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def print_evaluate(true, predicted):
    mae = metrics.mean_absolute_error(true, predicted)
    mse = metrics.mean_squared_error(true, predicted)
    rmse = np.sqrt(metrics.mean_squared_error(true, predicted))
    print('MAE:', mae)  # Minimum Absolute Error
    print('MSE:', mse)  # Mean Squared Error
    print('RMSE:', rmse)  # Root Mean Squared Error
    print(b.OK + '__________________________________' + b.END)


if __name__ == '__main__':
    housing_price = pd.read_csv('../USA_Housing.csv')

    print(housing_price.columns)

    ''' Analyze the data '''
    # sns.pairplot(housing_price)
    #
    # housing_price.hvplot.hist(by='Price', subplots=False, width=1000)
    # housing_price.hvplot.hist("Price")
    # housing_price.hvplot.scatter(x='Avg. Area House Age', y='Price')
    # housing_price.hvplot.scatter(x='Avg. Area Income', y='Price')
    # housing_price.columns
    # sns.heatmap(housing_price.corr(), annot=True)
    #
    # plt.show()

    ''' Train test split '''
    X = housing_price[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                       'Avg. Area Number of Bedrooms', 'Area Population']]
    y = housing_price['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # ''' Preprocessing '''
    # pipeline = Pipeline([
    #     ('std_scalar', StandardScaler())
    # ])
    #
    # X_train = pipeline.fit_transform(X_train)
    # X_test = pipeline.transform(X_test)

    ''' Linear Regression '''
    lin_reg = LinearRegression(normalize=True)
    lin_reg.fit(X_train, y_train)

    print(b.OK + 'Intercept : ' + b.END, lin_reg.intercept_)

    coeff_df = pd.DataFrame(lin_reg.coef_, X.columns, columns=['Coefficient'])
    print(b.OK + 'Coefficient' + b.END)
    print(coeff_df)

    ''' Predict '''
    pred = lin_reg.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': pred})
    print(b.OK + 'Prediction' + b.END)
    print(df)

    # Regression Evaluation
    print(b.OK + 'Set evaluation:\n_____________________________________' + b.END)
    print_evaluate(y_test, pred)
