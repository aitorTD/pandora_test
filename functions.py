import requests
import time
import os

url_pics = "https://jsonplaceholder.typicode.com/photos/"
url_albums = "https://jsonplaceholder.typicode.com/albums/"



def secuencial(photos):
    start_time = time.time()
    print("Modo de ejecucion: Secuencial")
    all_pics = requests.get(url_pics)
    all_albums = requests.get(url_albums)
    if all_pics.status_code == 200 and all_albums.status_code == 200:
        print("Success reciving data")
        all_pics = all_pics.json()
        all_albums = all_albums.json()
        album_dict = {album["id"]: album["title"] for album in all_albums}
        if photos == "all":
            # print("Enseño todas las fotos")
            for pic in all_pics:
                print(f"Pic ID: {pic['id']}")
                print(f"Title: {pic['title'].title()}")
                print(f"URL: {pic['url']}")
                print(f"Album ID: {pic['albumId']}")
                print(f"Album Title: {album_dict[pic['albumId']]}")
                print(" ")
        else:
            # print(f"Show {photos} pics")
            photos = int(photos)
            pics = all_pics[:photos]
            for pic in pics:
                print(f"Pic ID: {pic['id']}")
                print(f"Title: {pic['title'].title()}")
                print(f"URL: {pic['url']}")
                print(f"Album ID: {pic['albumId']}")
                print(f"Album Title: {album_dict[pic['albumId']]}")
                print(" ")
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
    else:
        print("Error reciving data")





def multihilo(photos):
    start_time = time.time()
    print("Modo de ejecucion: Multihilo")
    

def multiprocesos(photos):
    start_time = time.time()
    print("Modo de ejecucion: Multiprocesos")