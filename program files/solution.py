import serial
import time
import csv
from datetime import datetime
#need a total of 2880 lines of data
# Serial Configuration
serial_port = "COM8"
baud_rate = 9600

# Open the serial port and debug
try:
    ser = serial.Serial(serial_port, baud_rate, timeout=2)
    time.sleep(2)  # Allow the serial connection to initialize
except Exception as e:
    print(f"Failed to open serial port: {e}")
    ser = None

#local storage
csv_file = "collected_data.csv"

#header for the csv file for easier extract later on. also the order of collected data -> keep in mind when upload to API later on
try:
    with open(csv_file, "x", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "DHT_temperature", "DHT_humidity", "BME_temperature", "BME_pressure", "BME_humidity"])
except FileExistsError:
    pass


dht_data = None
bme_data = None

def save_to_csv(timestamp, dht_temp, dht_hum, bme_temp, bme_pres, bme_hum):
    with open(csv_file, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, dht_temp, dht_hum, bme_temp, bme_pres, bme_hum])


def process_data(line):
    global dht_data, bme_data

    try:
        parts = line.strip().split(',')
        sensor_type = parts[0]

        #timestamp
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Process DHT11 data
        if sensor_type == "DHT11":
            dht_humidity = float(parts[1]) if len(parts) > 1 else None
            dht_temp = float(parts[2]) if len(parts) > 2 else None
            dht_data = (dht_temp, dht_humidity)  #store the data temporarily
            print(f"DHT11 - Temperature: {dht_temp}, Humidity: {dht_humidity}")

        # Process BME280 data
        elif sensor_type == "BME280":
            bme_temp = float(parts[1]) if len(parts) > 1 else None
            bme_pressure = float(parts[2]) if len(parts) > 2 else None
            bme_humidity = float(parts[3]) if len(parts) > 3 else None
            bme_data = (bme_temp, bme_pressure, bme_humidity)  #store the data temporarily
            print(f"BME280 - Temperature: {bme_temp}, Pressure: {bme_pressure}, Humidity: {bme_humidity}")


        if dht_data and bme_data: #when both of them are collected, then save in the local file
            dht_temp, dht_humidity = dht_data
            bme_temp, bme_pressure, bme_humidity = bme_data
            save_to_csv(current_time, dht_temp, dht_humidity, bme_temp, bme_pressure, bme_humidity)
            print(f"Logged data: {current_time}, {dht_temp}, {dht_humidity}, {bme_temp}, {bme_pressure}, {bme_humidity}")

            dht_data = None
            bme_data = None
    #debug
    except (ValueError, IndexError) as e:
        print(f"Error processing line: {line}, Error: {e}")


try:
    if ser: #if serial port has been successfully opened and initialized.
        print("Listening for sensor data...")
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    process_data(line)

except KeyboardInterrupt:
    print("Stopping script.")
finally:
    if ser:
        ser.close()
