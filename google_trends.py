from pytrends.request import TrendReq


def init_google_trends():
    pytrend = TrendReq(hl='de', tz=360)
    return pytrend


def searches_for(pytrend, keyword, timeframe, region):
    pytrend.build_payload(kw_list=[keyword], cat=0, timeframe=timeframe, geo=region, gprop='')
    data = pytrend.interest_over_time()
    return data

