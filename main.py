import requests
import json
import time


def info():
    return requests.get("https://blockchain.info/ru/ticker").text


answer = input("Введите валюту: ")

while True:
    d = json.loads(info())
    d2 = d[answer]
    print(d2["buy"])
    time.sleep(5)
