import matplotlib.pyplot as plt


def plot_curve(data, keywords):
    for keyword in keywords:
        x_axis = []
        y_axis = []
        for index, value in data[keyword].items():
            x_axis.append(index)
            y_axis.append(value)
        plt.plot(x_axis, y_axis, label=keyword)
    plt.xlabel('Time')
    plt.ylabel('Level of Interest')
    plt.title('Interest over time')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
