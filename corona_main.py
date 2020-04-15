from google_trends import init_google_trends, searches_for
from plot import plot_curve

if __name__ == "__main__":
    pytrend = init_google_trends()
    keywords = ['desinfektionsmittel', 'seife', 'klopapier', 'mundschutz']
    data = searches_for(pytrend, keywords)
    plot_curve(data, keywords)

    keywords = ['corona', 'bundesliga', 'ausgangssperre', 'soforthilfe', 'italien']
    data = searches_for(pytrend, keywords)
    plot_curve(data, keywords)

    keywords = ['kinderbetreuung', 'schule', 'kita', 'alleinerziehend', 'notbetreuung']
    data = searches_for(pytrend, keywords)
    plot_curve(data, keywords)

    keywords = ['depression', 'mein mann schlägt mich', 'häusliche gewalt', 'seelsorge']
    data = searches_for(pytrend, keywords)
    plot_curve(data, keywords)


