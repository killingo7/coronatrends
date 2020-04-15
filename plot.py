import datetime
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_curve(y_axis, label="", timeframe=90, numyears=1):
    # x axis values: dates of the last n years (n defined above by the user)
    numdays = 7
    numweeks = 52
    total_time_range = numdays * numweeks * numyears

    end_date = date.today()
    begin_date = end_date - datetime.timedelta(days=total_time_range - 7)

    datelist = [begin_date]
    for index in range(0, numweeks * numyears - 3):
        datelist.append(datelist[index] + datetime.timedelta(days=numdays))
    x_axis = datelist
    print(datelist)
    # Plot into a chart
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(0, 14 * numyears))
    plt.gcf().autofmt_xdate()
    plt.plot(x_axis, y_axis, label=label)
    plt.xticks(rotation=45)
    plt.xlabel('Time')
    plt.ylabel('Level of Interest')
    plt.title('Interest over time')
    plt.legend()
    plt.show()
