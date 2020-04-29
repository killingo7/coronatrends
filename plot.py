import matplotlib.pyplot as plt
import pandas as pd


def make_axis_for_pytrends(data, keywords):
    output = {}
    for keyword in keywords:
        x_axis = []
        y_axis = []
        for index, value in data[keyword].items():
            x_axis.append(index)
            y_axis.append(value)
        output[keyword] = [x_axis, y_axis]
    return output


def make_axis_for_wiki(data, keyword):
    output = {}
    x_axis = []
    y_axis = []
    for d in data["items"]:
        timestamp = d["timestamp"]
        timestamp = timestamp[0:4] + "-" + timestamp[4:6] + "-" + timestamp[6:8]
        timestamp = pd.Timestamp(timestamp)
        x_axis.append(timestamp)
        y_axis.append(d["views"])
    output[keyword] = [x_axis, y_axis]
    return output


def plot_curve(data):
    for d in data:
        plt.plot(data[d][0], data[d][1], label=d)
    plt.xlabel('Time')
    plt.ylabel('Level of Interest')
    plt.title('Interest over time')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
