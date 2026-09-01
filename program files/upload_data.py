import csv
import socket
import time
import requests

# API Configuration
ip = "192.168.4.137"
user = {"username": "A_square", "password": "Ann&Annie"}
failure_count = 0


def check_connection(host=ip, port=80, timeout=3):
    # Check if the server is reachable.
    try:
        socket.setdefaulttimeout(timeout)
        socket.create_connection((host, port))
        return True
    except OSError:
        return False


def login():
    try:
        response = requests.post(f'http://{ip}/login', json=user)
        response.raise_for_status()  # Raise an error for failed login attempts
        cookie = response.json()["access_token"]
        auth = {"Authorization": f"Bearer {cookie}"}
        print("Login successful.")
        return auth
    except Exception as e:
        print(f"Failed to log in: {e}")
        return None


def upload_data(sensor_id, value, auth):
    try:
        url = f"http://{ip}/reading/new"
        payload = {
            "sensor_id": sensor_id,
            "value": value,
            "datetime": timestamp  # Include timestamp in the payload
        }
        response = requests.post(url, json=payload, headers=auth)

        if response.status_code == 200:
            print(f"Successfully uploaded sensor ID {sensor_id} with value {value}.")
            print(f"Server response: {response.json()}")
        else:
            print(f"Failed to upload sensor ID {sensor_id} with value {value}. Server response: {response.text}")
    except Exception as e:
        print(f"Error during upload: {e}")


def upload_data_from_csv(csv_file, sensor_ids):
    global failure_count, timestamp

    try:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                timestamp = row["timestamp"]
                print(f"Processing data for timestamp {timestamp}...")

                for field, sensor_id in sensor_ids.items():
                    value = row.get(field)
                    if value and value.lower() != "nan":
                        try:
                            value = float(value)

                            # Ensure server connection
                            if check_connection():
                                auth = login()
                                if not auth:
                                    print("Skipping upload due to failed login.")
                                    continue

                                upload_data(sensor_id, value, auth)
                            else:
                                print("Server connection failed. Retrying later...")
                                failure_count += 1
                                time.sleep(60)  # Wait before retrying
                        except ValueError:
                            print(f"Invalid value for {field}: {value}. Skipping upload.")
                        except Exception as e:
                            print(f"Unexpected error while processing {field}: {e}")
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
    except Exception as e:
        print(f"Error processing CSV file: {e}")


sensor_ids = {
    "DHT_temperature": 432,
    "DHT_humidity": 433,
    "BME_temperature": 434,
    "BME_pressure": 435,
    "BME_humidity": 436,
}

# Upload data from CSV
upload_data_from_csv(csv_file="final_data.csv", sensor_ids=sensor_ids)

print(f"The upload failed {failure_count} times.")
if failure_count > 0:
    print("How desperate!")
