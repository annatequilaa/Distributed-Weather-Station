from matplotlib.pyplot import subplots, fill_between

from graph_lib import *
import requests
from matplotlib import pyplot as plt
import numpy as np
plt.style.use('ggplot')

server_ip = "192.168.4.137"
data = {
    "temperature": [],
    "humidity": [],
    "pressure": [],
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
    if entry['sensor_id'] == 10:
        data["temperature"].append(entry["value"])
        data["time"].append(entry["datetime"])
        data["stripped_time"].append(entry["datetime"][11:-3])
        count += 1
    elif entry['sensor_id'] == 11:
        data["humidity"].append(entry["value"])
        count += 1
    elif entry['sensor_id'] == 12:
        data["pressure"].append(entry["value"])
        count += 1

data["temperature"] = data["temperature"][0:3000]
data["humidity"] = data["humidity"][0:3000]
data["pressure"] = data["pressure"][0:3000]
data["time"] = data["time"][0:3000]
#debugging
# print(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# minimum_len = min(len(data["time"]),len(data["temperature_DHT"]),len(data["humidity_DHT"]),len(data["temperature_BME"]),len(data["humidity_BME"]),len(data["pressure_BME"]))
# print(minimum_len)

#graph properties
fig = plt.figure(figsize=(12, 6))
gs = fig.add_gridspec(3, 1)
plt.subplots_adjust(hspace=0.7)
x = []
for i in range(len(data["time"])):
    x.append(i)

ws = 100

g1 = fig.add_subplot(gs[0, 0])
xT = data["time"]
yT = data["temperature"]
yT_smoothed = moving_average(ws,yT)
print(plot_data2(g1,xT,yT,"Temperature"," (°C)"))
g1.plot(xT[int(ws/2):len(yT_smoothed)+int(ws/2)],yT_smoothed,color="#577c8e")
print(plot_cub_model(yT))
g1.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'upper right', fontsize = 'x-small')

g2 = fig.add_subplot(gs[1, 0])
xH= data["time"]
yH = data["humidity"]
yH_smoothed = moving_average(ws,yH)
print(plot_data2(g2,xH,yH,"Humidity"," (%)"))
g2.plot(xH[int(ws/2):len(yH_smoothed)+int(ws/2)],yH_smoothed,color="#577c8e")
print(plot_cub_model(yH))
g2.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')

g3 = fig.add_subplot(gs[2, 0])
xP= data["time"]
yP = data["pressure"]
yP_smoothed = moving_average(ws,yP)
print(plot_data2(g3,xP,yP,"Pressure"," (hPa)"))
g3.plot(xP[int(ws/2):len(yP_smoothed)+int(ws/2)],yP_smoothed,color="#577c8e")
print(plot_cub_model(yP))
g3.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'upper right', fontsize = 'x-small')

plt.show()

plt.subplots_adjust(hspace=0.7, wspace=0.1)

a1 = plt.subplot(3,1,1)
xT = data["time"]
yT = data["temperature"]
yT_smoothed = moving_average(ws,yT)
print(plot_data2(a1,xT,yT,"Temperature"," (°C)"))
a1.plot(xT[int(ws/2):len(yT_smoothed)+int(ws/2)],yT_smoothed,color="#577c8e")

plot_cub_model(yT)
a1.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'upper right', fontsize = 'x-small')

a2 = plt.subplot(3,1,2)
xH= data["time"]
yH = data["humidity"]
yH_smoothed = moving_average(ws,yH)
print(plot_data2(a2,xH,yH,"Humidity"," (%)"))
a2.plot(xH[int(ws/2):len(yH_smoothed)+int(ws/2)],yH_smoothed,color="#577c8e")
print(plot_cub_model(yH))
a2.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'lower right', fontsize = 'x-small')

a3 = plt.subplot(3,1,3)
xP= data["time"]
yP = data["pressure"]
yP_smoothed = moving_average(ws,yP)
print(plot_data2(a3,xP,yP,"Pressure"," (hPa)"))
a3.plot(xP[int(ws/2):len(yP_smoothed)+int(ws/2)],yP_smoothed,color="#577c8e")
print(plot_cub_model(yP))
a3.legend(['raw data', 'smoothed data', 'cubic model'],loc = 'upper right', fontsize = 'x-small')

plt.show()

stats_temp = calc_statistics(data["temperature"])
stats_hum = calc_statistics(data["humidity"])
stats_pre = calc_statistics(data["pressure"])

plt.subplots_adjust(hspace=0.7, wspace=0.1)

temp_stats = plt.subplot(3, 1, 1)
plot_data(temp_stats, data["time"], data["temperature"], "Temperature Statistics", " (°C)")
temp_stats.plot(data["time"][int(ws/2):len(yT_smoothed)+int(ws/2)],yT_smoothed,color="#577c8e")
temp_stats.axhline(stats_temp["median"], color='green', linestyle='--', label='median')
temp_stats.axhline(stats_temp["min"], color='purple', linestyle='--', label='min')
temp_stats.axhline(stats_temp["max"], color='orange', linestyle='--', label='max')
temp_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

hum_stats = plt.subplot(3, 1, 2)
plot_data(hum_stats, data["time"], yH, "Humidity Statistics", " (%)")
hum_stats.plot(data["time"][int(ws/2):len(yH_smoothed)+int(ws/2)],yH_smoothed,color="#577c8e")
hum_stats.axhline(stats_hum["median"], color='green', linestyle='--', label='median')
hum_stats.axhline(stats_hum["min"], color='purple', linestyle='--', label='min')
hum_stats.axhline(stats_hum["max"], color='orange', linestyle='--', label='max')
hum_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

pre_stats = plt.subplot(3, 1, 3)
plot_data(pre_stats,data["time"],yP,"Pressure"," (hPa)")
pre_stats.plot(data["time"][int(ws/2):len(yP_smoothed)+int(ws/2)],yP_smoothed,color="#577c8e")
pre_stats.axhline(stats_pre["median"], color='green', linestyle='--', label='median')
pre_stats.axhline(stats_pre["min"], color='purple', linestyle='--', label='min')
pre_stats.axhline(stats_pre["max"], color='orange', linestyle='--', label='max')
pre_stats.legend(['raw data', 'smoothed data','median', 'min','max'], loc='upper right', fontsize='x-small')

plt.show()
