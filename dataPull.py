#!/usr/bin/env python
##This script is for pulling actors names from the Rotten Tomatoes API. It then checks for common actors in a pair of films it is executed from the shell with arguments like 'dataPull.py "50 First Dates" "E.T."' Which would return: Actors in 50 First Dates and E.T. set([u'Drew Barrymore'])


import sys
import json
import urllib
import urllib2
import getpass
import databasepull
import MySQLdb as mdb

baseurl = "http://api.rottentomatoes.com/api/public/v1.0.json"
apikey = "?apikey=6rst6markqmfj86ab9ssgm6m"

## connection takes ip address, username, password and database
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

jsonresponse = urllib2.urlopen(baseurl+apikey).read()
jsonobj = json.loads(jsonresponse)

##TODO(max) This  is one extra external call. could remove it in favour of pointing straight to movies.
moviesurl = jsonobj["links"]["movies"]
listsurl = jsonobj["links"]["lists"]

def fetchCast(filmname):
  """Checks if we have film and if not fetchs it online and stores it."""
  characterset = databasepull.checkFilmDatabase(filmname, con)
  if characterset:
    print "fetched locally"
    return characterset
  else:
    characterset = fetchCastOnline(filmname)
    databasepull.storeFilmDatabase(filmname, characterset, con)
    print "fetched online"
    
    return characterset    


def fetchCastOnline(filmname):
  """This function takes a fimname as a  string and returns a set of actor names from that films"""
  encodedFilm = urllib.quote(filmname)
  query = "&q="+encodedFilm+"&page_limit=1"
  jsonresponse = urllib2.urlopen(moviesurl+apikey+query).read()
  jsonobj = json.loads(jsonresponse)
  characterset = set([])
  try:
    castlink= jsonobj["movies"][0]["links"]["cast"]
    jsonresponse = urllib2.urlopen(castlink+apikey).read()
    jsonobj = json.loads(jsonresponse)
    characters = jsonobj["cast"]
    for inidividual in characters:
      name = inidividual["name"]
      characterset.add(name)
  except IndexError:
    print "Error film not found. Please check title spelling"

  return(characterset)


def findIntersection(actorSetA, actorSetB):
  """This function takes two sets of actor names and returns their intersection. This could be two films actors or two pairs of overlaps depending on the use case"""
  overlap = actorSetA.intersection(actorSetB)
  overlap
  return(overlap)

def decideRunType(film1="",film2=""):
  if film1 =="" and film2 =="":
    print "Please input one film name to see the list of actors in that film or two film names seperated by a space to see what actors are in both films"
    print ""
    print "An example would by dataPull.py \"The Dallas Buyers Club\" \"Interstellar\" "
    print "The quotation marks are not necessary unless there are spaces in the film names"
    return set([]) 
  elif film2=="":
    print "Actors in "+film1
    cast = fetchCast(film1)
    print cast
    return cast
  else:
    print "Actors in "+film1+" and "+film2
    castA = fetchCast(film1)
    castB = fetchCast(film2)
    intersection= findIntersection(castA,castB)
    print intersection
    return intersection

def main():
  inputs = len(sys.argv)-1
  if not databasepull.checkFilmDatabaseExists(con):
    databasepull.createDatabaseTable(con)
  if not databasepull.checkLogDatabaseExists(con):
    databasepull.createDatabaseLogTable(con)
  databasepull.logDatabaseActivity(con,"command-line",getpass.getuser(),str(sys.argv))
  if inputs ==0:
    decideRunType()
  elif inputs ==1:
    decideRunType(str(sys.argv[1]).strip())
  elif inputs ==2:
    decideRunType(str(sys.argv[1]).strip(),str(sys.argv[2]).strip())
  else:
    print "Error: Too many inputs"
    print "Please use one film name to see the actors in that film or two film names to see the actors specifically in both"

if __name__ == "__main__":main() ## with if

