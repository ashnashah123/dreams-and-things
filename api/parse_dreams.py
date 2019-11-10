from bs4 import BeautifulSoup
import os
import requests


path = "Dreams"

listDreams = []
for filename in os.listdir(path):
    print(filename)
    with open(path + "/" + filename, 'r') as file:
        data = file.read()
        listDreams.append(data)

for dream in listDreams:
    soup = BeautifulSoup(dream)
    print(soup.title)

