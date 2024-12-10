import random
from time import sleep
from requests import post


MAX_TEMP = 37.0
MIN_T_BETWEEN_WARNING = 60

BASE_URL = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update"
api_key="OVVCSEUBGDB29965"


def send_notification(temp):
    status = f"Raspberry Pi getting hot. CPU temp = {str(temp)}"
    data = {"api_key": api_key, "status": status}
    post(url=BASE_URL, data=data)


def cpu_temp():
    cpu_temp = random.randint(1, 100)
    return cpu_temp

while True:
    temp = cpu_temp()
    print(f"CPU Temp (C): {str(temp)}")
    if temp > MAX_TEMP:
        print("CPU TOO HOT!")
        send_notification(temp)
        print(f"No more notifications for: {str(MIN_T_BETWEEN_WARNING)} minutes")
    sleep(MIN_T_BETWEEN_WARNING)
