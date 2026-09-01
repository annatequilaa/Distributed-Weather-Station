import requests
from datetime import datetime


ip = "192.168.4.137"
request = requests.get(f"http://{ip}/readings")

user = {"username": "A_square", "password": "Ann&Annie"}
r = requests.post(f"http://{ip}/register", json = user)

answer = requests.post(f'http://{ip}/login', json=user)
cookie = answer.json()["access_token"]
print(cookie)

auth = {"Authorization": f"Bearer {cookie}"}

final_dht_t = {"type": "Temperature",
        "location": "R3-10",
        "name": "asquare_dht_1",
        "unit": "C"} #id: 432
r = requests.post(f'http://{ip}/sensor/new', json=final_dht_t, headers=auth)

final_dht_h = {"type": "Humidity",
        "location": "R3-10",
        "name": "asquare_dht_2",
        "unit": "%"} #id: 433

r = requests.post(f'http://{ip}/sensor/new', json=final_dht_h, headers=auth)
final_bme_t = {"type": "Temperature",
        "location": "R3-10",
        "name": "asquare_bme_1",
        "unit": "C"} #id: 434

r = requests.post(f'http://{ip}/sensor/new', json=final_bme_t, headers=auth)
final_bme_h = {"type": "Humidity",
        "location": "R3-10",
        "name": "asquare_bme_2",
        "unit": "%"} #id: 435

r = requests.post(f'http://{ip}/sensor/new', json=final_bme_h, headers=auth)

final_bme_p = {"type": "Pressure",
        "location": "R3-10",
        "name": "asquare_bme_3",
        "unit": "hPa"} #id: 436
r = requests.post(f'http://{ip}/sensor/new', json=final_bme_p, headers=auth)

