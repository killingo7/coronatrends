from google_trends import init_google_trends, searches_for
from plot import plot_curve

if __name__ == "__main__":
    pytrend = init_google_trends()
    keyword = 'covid-19'
    data = searches_for(pytrend, keyword, 'today 3-m', 'DE-BW')
    plot_curve(data[keyword])

