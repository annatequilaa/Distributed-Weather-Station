from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')

# temperature, humidity, pressure = []
#
# print(temperature)
# print(humidity)
# print(pressure)

# data = {
#     "temperature": [values],
#     "humidity": [values],
#     "pressure": [values],
# }

def moving_average(windowSize:int, x:list) -> list:
    x_smoothed = []
    for i in range(0,len(x)-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section)/windowSize
        x_smoothed.append(x_average)
    return x_smoothed


# def cub(a, b, c, d, e, f, g, h, i, x):
#     return a * x ** 8 + b * x ** 7 + c * x ** 6 + d * x ** 5 + e * x ** 4 + f * x ** 3 + g * x ** 2 + h * x + i
#
#
# def plot_cub_model(value):
#     x = [i for i in range(len(value))]
#     coefficients = np.polyfit(x, value, 8)
#     x_model = np.linspace(min(x), max(x), 500)
#     y_model = np.polyval(coefficients, x_model)
#     plt.plot(x_model, y_model,color="#bf8f90")
#     return "Cubic model plotted successfully"

def cub(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def plot_cub_model(value):
    x = [i for i in range(len(value))]
    coefficients = np.polyfit(x, value, 3)
    x_model = np.linspace(min(x), max(x), 500)
    y_model = np.polyval(coefficients, x_model)
    plt.plot(x_model, y_model,color="#9b495d")
    return "Cubic model plotted successfully"

def get_avg(v1,v2):
    avg = []
    if len(v1)>len(v2):
        for i in range(len(v2)):
            avg.append((v1[i]+v2[i])/2)
    else:
        for i in range(len(v1)):
            avg.append((v1[i]+v2[i])/2)
    return (avg)


# mean, standard deviation, minimum, maximum, and median
def calc_statistics(values):
    stats = {
        "std_dev": np.std(values),
        "mean": np.mean(values),
        "min": np.min(values),
        "max": np.max(values),
        "median": np.median(values),
    }
    return stats

def standard_deviation(x,y,sub):
    mean = []
    std = []


    for i in y:
        mean.append(np.mean(i))
        std.append(np.std(i))
    sub.errorbar(x, mean, std, fmt="o")
    sub.fill_between(x, max(y), min(y), alpha=0.5, linewidth=0, color="#8ecae6")


def plot_data(subplot,x:list,y:list, ylabel,yunits):
    subplot.plot(x,y,color = "#c7d9e5")
    subplot.set_title(ylabel)
    subplot.set_xlabel("Time (hr)")
    subplot.set_ylabel(ylabel+yunits)
    x_l = []
    for t in range(len(x)):
        if (t)%360 == 0 and t+13<=len(x):
            x_l.append(x[t+13][11:-3])
    subplot.set_xticklabels(x_l)
    subplot.set_xticks(np.arange(13, len(x) + 1,360))
    return("data plotted successfully")

def plot_data1(subplot,x:list,y:list, ylabel,yunits):
    subplot.plot(x,y,color = "#2b9b35",linewidth=0.5)
    subplot.set_title(ylabel)
    subplot.set_xlabel("Time (hr)")
    subplot.set_ylabel(ylabel+yunits)
    x_l = []
    for t in range(len(x)):
        if (t)%360 == 0 and t+13<=len(x):
            x_l.append(x[t+13][11:-3])
    subplot.set_xticklabels(x_l)
    subplot.set_xticks(np.arange(13, len(x) + 1,360))
    return("data plotted successfully")

def plot_data2(subplot,x:list,y:list, ylabel,yunits):
    subplot.plot(x,y,color = "#2b9b35",linewidth=0.5)
    subplot.set_title(ylabel)
    subplot.set_xlabel("Time (hr)")
    subplot.set_ylabel(ylabel+yunits)
    x_l = []
    for t in range(len(x)):
        if (t)%360== 0 and t<=len(x):
            x_l.append(x[t][11:-10])
    subplot.set_xticklabels(x_l)
    subplot.set_xticks(np.arange(0, len(x) + 1,360))
    return("data plotted successfully")

