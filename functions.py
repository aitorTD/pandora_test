import requests
import time
import os

url_pics = "https://jsonplaceholder.typicode.com/photos/"

def secuencial(photos):
    pics = requests.get(url_pics)
    if pics.status_code == 200:
        print("Success reciving data")
    else:
        print("Error reciving data")

def multihilo(photos):
    pass

def multiprocesos(photos):
    pass