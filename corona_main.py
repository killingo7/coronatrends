from google_trends import init_google_trends, searches_for
from plot import plot_curve, make_axis_for_pytrends, make_axis_for_wiki
from wikipedia import wiki_visits

if __name__ == "__main__":
    pytrend = init_google_trends()
    keywords = ['desinfektionsmittel', 'seife', 'klopapier', 'mundschutz']
    data = searches_for(pytrend, keywords)
    data = make_axis_for_pytrends(data, keywords)
    plot_curve(data)

    keywords = ["Suizid_durch_Vergiftung_mit_Medikamenten", "Suizid_durch_Sprung_aus_der_Höhe"]
    plot_data = {}
    for keyword in keywords:
        data = wiki_visits(keyword, "2019100100", "2020042800")
        if data:
            data = make_axis_for_wiki(data, keyword)
            plot_data.update(data)

    plot_curve(plot_data)


