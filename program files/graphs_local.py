from matplotlib.pyplot import subplots, fill_between

from graph_lib import *
import requests
from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')

server_ip = "192.168.4.137"
data = {
    "temperature_DHT": [],
    "humidity_DHT": [],
    "temperature_BME": [],
    "humidity_BME": [],
    "pressure_BME": [],
    "time":[],
    "stripped_time":[]
}

request = requests.get(f"http://{server_ip}/readings")
d = request.json()
readings = d['readings'][0]
count = 0

for entry in readings:
    # if count == 14425:
    #     break
    if entry['sensor_id'] == 432:
        data["temperature_DHT"].append(entry["value"])
        data["time"].append(entry["datetime"])
        data["stripped_time"].append(entry["datetime"][11:-3])
        count += 1
    elif entry['sensor_id'] == 433:
        data["humidity_DHT"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 434:
        data["temperature_BME"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 436:
        data["humidity_BME"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 435:
        data["pressure_BME"].append(entry["value"])
        count += 1

data["temperature_DHT"] = data["temperature_DHT"][0:2950]
data["humidity_DHT"] = data["humidity_DHT"][0:2950]
data["temperature_BME"] = data["temperature_BME"][0:2950]
data["humidity_BME"] = data["humidity_BME"][0:2950]
data["pressure_BME"] = data["pressure_BME"][0:2950]
data["time"] = data["time"][0:2950]
data["stripped_time"] = data["stripped_time"][0:2950]
#debugging
# print(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# minimum_len = min(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# print(minimum_len)

#graph properties
fig = plt.figure(figsize=(12, 6))
gs = fig.add_gridspec(3, 2)
plt.subplots_adjust(hspace=0.7)
x = []
for i in range(len(data["time"])):
    x.append(i)

ws = 100

#DHT graphs
#temp
g1 = fig.add_subplot(gs[0, 0])
xDT = data["time"]
yDT = data["temperature_DHT"]
yDT_smoothed = moving_average(ws,yDT)
print(plot_data(g1,xDT,yDT,"Temperature (DHT)"," (°C)"))
g1.plot(xDT[int(ws/2):len(yDT_smoothed)+int(ws/2)],yDT_smoothed,color="#577c8e")
print(plot_cub_model(yDT))
g1.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')

#hum

g2 = fig.add_subplot(gs[1, 0])
xDH= data["time"]
yDH = data["humidity_DHT"]
yDH_smoothed = moving_average(ws,yDH)
print(plot_data(g2,xDH,yDH,"Humidity (DHT)"," (%)"))
g2.plot(xDH[int(ws/2):len(yDH_smoothed)+int(ws/2)],yDH_smoothed,color="#577c8e")
print(plot_cub_model(yDH))
g2.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'upper right', fontsize = 'x-small')

#BME
#temp
g3 = fig.add_subplot(gs[0, 1])
xBT= data["time"]
yBT = data["temperature_BME"]
yBT_smoothed = moving_average(ws,yBT)
print(plot_data(g3,xBT,yBT,"Temperature (BME)"," (°C)"))
g3.plot(xBT[int(ws/2):len(yBT_smoothed)+int(ws/2)],yBT_smoothed,color="#577c8e")
print(plot_cub_model(yBT))
g3.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')


#hum
g4 = fig.add_subplot(gs[1, 1])
xBH= data["time"]
yBH = data["humidity_BME"]
yBH_smoothed = moving_average(ws,yBH)
print(plot_data(g4,xBH,yBH,"Humidity (BME)"," (%)"))
g4.plot(xBH[int(ws/2):len(yBH_smoothed)+int(ws/2)],yBH_smoothed,color="#577c8e")
print(plot_cub_model(yBH))
g4.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')


#pressure
g5 = fig.add_subplot(gs[2, 1])
xBP= data["time"]
yBP = data["pressure_BME"]
yBP_smoothed = moving_average(ws,yBP)
print(plot_data(g5,xBP,yBP,"Pressure (BME)"," (hPa)"))
g5.plot(xBP[int(ws/2):len(yBP_smoothed)+int(ws/2)],yBP_smoothed,color="#577c8e")
print(plot_cub_model(yBP))
g5.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')

plt.show()

#avg plots below

plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
avg1 = get_avg(data["temperature_DHT"],data["temperature_BME"])
plot_data(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1_smoothed = moving_average(ws,avg1)
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
a1.legend(['raw data', 'smoothed data'],loc = 'lower right', fontsize = 'x-small')


a2 = plt.subplot(3,1,2)
avg2 = get_avg(data["humidity_DHT"],data["humidity_BME"])
plot_data(a2, data["time"],avg2,"Average Humidity"," (%)")
a2_smoothed = moving_average(ws,avg2)
a2.plot(data["time"][int(ws/2):len(a2_smoothed)+int(ws/2)],a2_smoothed,color="#577c8e")
a2.legend(['raw data', 'smoothed data'],loc = 'upper right', fontsize = 'x-small')

a3 = plt.subplot(3,1,3)
avg3 = data["pressure_BME"]
plot_data(a3, data["time"],avg3,"Pressure (BME)"," (hPa)")
a3_smoothed = moving_average(ws,avg3)
a3.plot(data["time"][int(ws/2):len(a3_smoothed)+int(ws/2)],a3_smoothed,color="#577c8e")
a3.legend(['raw data', 'smoothed data'],loc = 'upper right', fontsize = 'x-small')

plt.show()


plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
plot_data(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
plot_cub_model(avg1)
a1.legend(['raw data', 'smoothed data','cubic model'],loc = 'lower right', fontsize = 'x-small')

a2 = plt.subplot(3,1,2)
plot_data(a2, data["time"],avg2,"Average Humidity"," (%)")
a2.plot(data["time"][int(ws/2):len(a2_smoothed)+int(ws/2)],a2_smoothed,color="#577c8e")
plot_cub_model(avg2)
a2.legend(['raw data', 'smoothed data','cubic model'],loc = 'upper right', fontsize = 'x-small')

a3 = plt.subplot(3,1,3)
plot_data(a3, data["time"],avg3,"Pressure (BME)"," (hPa)")
a3.plot(data["time"][int(ws/2):len(a3_smoothed)+int(ws/2)],a3_smoothed,color="#577c8e")
plot_cub_model(avg3)
a3.legend(['raw data', 'smoothed data','cubic model'],loc = 'upper right', fontsize = 'x-small')

plt.show()


stats_temp = calc_statistics(avg1)
stats_hum = calc_statistics(avg2)
stats_pre = calc_statistics(avg3)

plt.subplots_adjust(hspace=0.7, wspace=0.1)

temp_stats = plt.subplot(3, 1, 1)
plot_data(temp_stats, data["time"], avg1, "Temperature Statistics", " (°C)")
temp_stats.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
temp_stats.axhline(stats_temp["median"], color='green', linestyle='--', label='median')
temp_stats.axhline(stats_temp["min"], color='purple', linestyle='--', label='min')
temp_stats.axhline(stats_temp["max"], color='orange', linestyle='--', label='max')
temp_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

hum_stats = plt.subplot(3, 1, 2)
plot_data(hum_stats, data["time"], avg2, "Humidity Statistics", " (%)")
hum_stats.plot(data["time"][int(ws/2):len(a2_smoothed)+int(ws/2)],a2_smoothed,color="#577c8e")
hum_stats.axhline(stats_hum["median"], color='green', linestyle='--', label='median')
hum_stats.axhline(stats_hum["min"], color='purple', linestyle='--', label='min')
hum_stats.axhline(stats_hum["max"], color='orange', linestyle='--', label='max')
hum_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

pre_stats = plt.subplot(3, 1, 3)
plot_data(pre_stats, data["time"], avg3, "Pressure Statistics", " (hPa)")
pre_stats.plot(data["time"][int(ws/2):len(a3_smoothed)+int(ws/2)],a3_smoothed,color="#577c8e")
pre_stats.axhline(stats_pre["median"], color='green', linestyle='--', label='median')
pre_stats.axhline(stats_pre["min"], color='purple', linestyle='--', label='min')
pre_stats.axhline(stats_pre["max"], color='orange', linestyle='--', label='max')
pre_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

plt.show()

plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
plot_data1(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
a1.fill_between(data["time"], avg1 - stats_temp["std_dev"], avg1 + stats_temp["std_dev"], alpha=0.5, color="#91bcd9", label="Standard Deviation Region")
a1.legend(['raw data', 'smoothed data','error bars'],loc = 'lower right', fontsize = 'x-small')

a2 = plt.subplot(3,1,2)
plot_data1(a2, data["time"],avg2,"Average Humidity"," (%)")
a2.plot(data["time"][int(ws/2):len(a2_smoothed)+int(ws/2)],a2_smoothed,color="#577c8e")
a2.fill_between(data["time"], avg2 - stats_hum["std_dev"], avg2 + stats_hum["std_dev"], alpha=0.5, color="#91bcd9", label="Standard Deviation Region")
a2.legend(['raw data', 'smoothed data','error bars'],loc = 'upper right', fontsize = 'x-small')

a3 = plt.subplot(3,1,3)
plot_data1(a3, data["time"],avg3,"Pressure"," (hPa)")
a3.plot(data["time"][int(ws/2):len(a3_smoothed)+int(ws/2)],a3_smoothed,color="#577c8e")
a3.fill_between(data["time"], avg3 - stats_pre["std_dev"], avg3 + stats_pre["std_dev"], alpha=0.5, color="#91bcd9", label="Standard Deviation Region")
a3.legend(['raw data', 'smoothed data','error bars'],loc = 'upper right', fontsize = 'x-small')

plt.show()


current_time = len(data["time"])
future_time = np.arange(current_time, current_time + 12 * 60)
x_data1 = np.arange(len(data["time"]))
y_data1 = avg1
coefficients1 = np.polyfit(x_data1, y_data1, 3)
predicted_values1 = cub(coefficients1[0], coefficients1[1], coefficients1[2], coefficients1[3], future_time)

plt.subplots_adjust(hspace=0.7, wspace=0.1)
a1 = plt.subplot(3,1,1)
plot_data(a1,data["time"],avg1,"Average Temperature"," (°C)")
a1.plot(data["time"][int(ws/2):len(a1_smoothed)+int(ws/2)],a1_smoothed,color="#577c8e")
xticks = np.concatenate([data["time"], future_time])
# a1.set_xticks(xticks[::360])
# a1.set_xticklabels(xticks[::360])
plot_cub_model(avg1)
plt.plot(future_time, predicted_values1, color="#bf8f90", linestyle='--')
a1.legend(['raw data', 'smoothed data',"cubic model", "predicted data (next 12 hours)"],loc = 'lower right', fontsize = 'x-small')

x_data2 = np.arange(len(data["time"]))
y_data2 = avg2
coefficients2 = np.polyfit(x_data2, y_data2, 3)
predicted_values2 = cub(coefficients2[0], coefficients2[1], coefficients2[2], coefficients2[3], future_time)
a2 = plt.subplot(3,1,2)
plot_data(a2, data["time"],avg2,"Average Humidity"," (%)")
a2.plot(data["time"][int(ws/2):len(a2_smoothed)+int(ws/2)],a2_smoothed,color="#577c8e")
# a1.set_xticks(xticks[::360])
# a1.set_xticklabels(xticks[::360])
plot_cub_model(avg2)
plt.plot(future_time, predicted_values2, color="#bf8f90", linestyle='--')
a2.legend(['raw data', 'smoothed data',"cubic model", "predicted data (next 12 hours)"],loc = 'upper right', fontsize = 'x-small')

x_data3 = np.arange(len(data["time"]))
y_data3 = avg3
coefficients3 = np.polyfit(x_data3, y_data3, 3)
predicted_values3 = cub(coefficients3[0], coefficients3[1], coefficients3[2], coefficients3[3], future_time)
a3 = plt.subplot(3,1,3)
plot_data(a3, data["time"],avg3,"Pressure"," (hPa)")
a3.plot(data["time"][int(ws/2):len(a3_smoothed)+int(ws/2)],a3_smoothed,color="#577c8e")
# a1.set_xticks(xticks[::360])
# a1.set_xticklabels(xticks[::360])
plot_cub_model(avg3)
plt.plot(future_time, predicted_values3, color="#bf8f90", linestyle='--')
a3.legend(['raw data', 'smoothed data',"cubic model", "predicted data (next 12 hours)"],loc = 'lower right', fontsize = 'x-small')



plt.show()
