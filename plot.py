import matplotlib.pyplot as plt


def plot_curve(data):
    x_axis = []
    y_axis = []
    for index, value in data.items():
        y_axis.append(index)
        x_axis.append(value)
        print(f"Index : {index}, Value : {value}")
    plt.plot(y_axis, x_axis)
    plt.xlabel('Time')
    plt.ylabel('Level of Interest')
    plt.title('Interest over time')
    plt.show()
