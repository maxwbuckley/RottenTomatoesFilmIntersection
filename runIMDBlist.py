import os

imdb = open("imdbmovielist.txt","r")
for line in imdb:
  os.system("python dataPull.py '"+line+"'")

