from google_trends import init_google_trends, searches_for
from plot import plot_curve

if __name__ == "__main__":
    pytrend = init_google_trends()
    data = searches_for(pytrend, 'covid-19', 'today 3-m', 'DE-BW')
    print(data.iloc[2, 0])
    plot_curve(data.iloc[:, 1], data.iloc[:, 0])

