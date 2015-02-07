#!/usr/bin/python

import MySQLdb as mdb


def checkFilmDatabase(FilmName, Connection):
  """Checks if we already have the meta data for this particular film stored in 
   our local database"""

  with Connection: 

    cur = Connection.cursor()
    cur.execute("SELECT ActorName FROM FilmActors WHERE FilmName='"+FilmName+"';")

    rows = cur.fetchall()
    characterset = set([])
    for row in rows:
        characterset.add(row[0])
    return characterset

def storeFilmDatabase(FilmName, ActorSet, Connection):
  with Connection:
    
    cur = Connection.cursor()
    for Actor in ActorSet:
      datadict = {"FilmName":FilmName, "Actor":Actor.replace("'","\\'")}
      string= "INSERT INTO FilmActors(FilmName,ActorName) VALUES('%(FilmName)s','%(Actor)s')" % datadict
      cur.execute(string)

def checkFilmDatabaseExists(Connection):
  """Checks if we already have set up the database with our table"""

  with Connection:
    cur = Connection.cursor()
    cur.execute(" SHOW TABLES LIKE '%%FilmActors%%'")
    rows = cur.fetchall()
    for row in rows:
      #print row[0]
      if(row[0]) =="FilmActors":
        return True
    return False

def createDatabaseTable(Connection):
  """Sets up our database table or resets it"""
  with Connection:
    cur = Connection.cursor()
    cur.execute("DROP TABLE IF EXISTS FilmActors")
    cur.execute("CREATE TABLE FilmActors(Id INT PRIMARY KEY AUTO_INCREMENT, Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                  FilmName VARCHAR(256), ActorName VARCHAR(256))")

def createDatabaseLogTable(Connection):
  """Sets up our database log table or resets it"""
  with Connection:
    cur = Connection.cursor()
    cur.execute("DROP TABLE IF EXISTS RottenTomatoesLog")
    cur.execute("CREATE TABLE RottenTomatoesLog(Id INT PRIMARY KEY AUTO_INCREMENT, Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, \
                  Source VARCHAR(256), User VARCHAR(256), Inputs VARCHAR(512))")

def logDatabaseActivity(Connection, Source, User, Inputs):
  """Records Activity"""
  with Connection:
    cur = Connection.cursor()
    datadict = {"Source":Source, "User":User.replace("'","\\'"), "Inputs":Inputs.replace("'","\\'")}
    string= "INSERT INTO RottenTomatoesLog(Source, User, Inputs) VALUES('%(Source)s','%(User)s','%(Inputs)s')" % datadict
    cur.execute(string)

def checkLogDatabaseExists(Connection):
  """Checks if we already have set up the logs database with our table"""

  with Connection:
    cur = Connection.cursor()
    cur.execute(" SHOW TABLES LIKE '%%RottenTomatoesLog%%'")
    rows = cur.fetchall()
    for row in rows:
      #print row[0]
      if(row[0]) =="RottenTomatoesLog":
        return True
    return False

