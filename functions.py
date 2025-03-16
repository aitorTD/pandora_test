import requests
import time
import os

url_pics = "https://jsonplaceholder.typicode.com/photos/"
url_albums = "https://jsonplaceholder.typicode.com/albums/"

def secuencial(photos):
    all_pics = requests.get(url_pics)
    all_albums = requests.get(url_albums)
    if all_pics.status_code == 200 and all_albums.status_code == 200:
        print("Success reciving data")
        all_pics = all_pics.json()
        all_albums = all_albums.json()
        if photos == "all":
            print("Enseño todas las fotos")



        else:
            # print(f"Enseño {photos} fotos")
            photos = int(photos)
            pics = all_pics[:photos]
            for pic in pics:
                print(f"Foto ID: {pic['id']}")
                print(f"Título: {pic['title'].title()}")
                print(f"URL: {pic['url']}")
                print(" ")
                # print(f"Album ID: {foto['albumId']}")
    else:
        print("Error reciving data")

def multihilo(photos):
    pass

def multiprocesos(photos):
    pass