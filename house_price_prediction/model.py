import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import hvplot.pandas

if __name__ == '__main__':
    housing_price = pd.read_csv('../USA_Housing.csv')

    print(housing_price.columns)

    ''' Analyze the data '''
    sns.pairplot(housing_price)

    housing_price.hvplot.hist(by='Price', subplots=False, width=1000)
    housing_price.hvplot.hist("Price")
    housing_price.hvplot.scatter(x='Avg. Area House Age', y='Price')
    housing_price.hvplot.scatter(x='Avg. Area Income', y='Price')
    housing_price.columns
    sns.heatmap(housing_price.corr(), annot=True)

    plt.show()
