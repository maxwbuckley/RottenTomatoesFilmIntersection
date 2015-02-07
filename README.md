#Rotten Tomatoes Intersection

This script is for pulling actors names from the Rotten Tomatoes API. It then checks for common actors in a pair of films it is executed from the shell with arguments. execute the script and supply it one or two  film names.

For example:

```sh
$ dataPull.py "50 First Dates" "E.T." 
```
Which would return: 
```sh
Actors in 50 First Dates and "E.T. 
set([u'Drew Barrymore'])
```

Or if supplied with only one film name like so

```sh
$ dataPull.py "Independence Day" 
```

Would return an set (unsorted) of the actors in that film.
```sh
Actors in Independence Day
set([u'Steve Giannell', u'Anthony Crivello', u'Barry Nolan', u"Capt. Michael 'Chewy' Vacca", u'Jon Matthews', u'Ernie Anastos', u'Thom Barry', u'Eric Paskel', u'Randy Quaid', u'Michael G. Moertl', u'Troy Willis', u'Dexter Warren', u'Jon Mathews', u'Marisa Morell', u'Deenie Dakota', u'Jay Acovone', u'Lisa Jakub', u'Barry Del Sherman', u'Cinckevin Cooney', u'Jeff Phillips', u'Morton Kondracke', u'Devon Gummersall', u'Vivica A. Fox', u'Bobby Hosea', u'Dakota', u'James J. Joyce', u'George Putnam', u'Barbara Beck', u'James Rebhorn', u'Harvey Fierstein', u'Will Smith', u'Rance Howard', u'Levani', u'Derek Kim', u'Gary W. Cruz', u'Thomas F. Duffy', u'Jim Piddock', u'Brent Spiner', u'Fred Barnes', u'David Pressman', u'Mary McDonnell', u'Kevin Sifuentes', u'Judd Hirsch', u'James Duval', u'Yelena Danova', u'Paul LeClair', u'Jessika Cardinahl', u'Mark Thompson', u'Kiersten Warren', u'Mark Fite', u'Ross Lacy', u'Ron Pitts', u'Jack Germond', u'Joe Fowler', u'Sayed Badreya', u'David Chanel', u'Ross Bagley', u'Julie Moran', u'Carlos Lara', u'Brooks Arthur', u'Carlos Lacamara', u'Lyman Ward', u'Greg Collins', u'Steve Giannelli', u'Jerry Dunphy', u'Eleanor Clift', u'Margaret Colin', u'Raphael Sbarge', u'Derek Webster', u'Mike Monteleone', u'Wendy Walsh', u'Tim Kelleher', u'Matt Pashkow', u'Christine Devine', u'Malcom Danare', u'Jana Marie Hupp', u'Bill Smitrovich', u'Vivian Palermo', u'Robert Loggia', u'Dan Lauria', u'Richard Speight Jr', u'Wayne Wilderson', u'Richard Pachorek', u'Joyce Cohen', u'Bill Pullman', u'Harry Connick Jr.', u'Elston Ridgle', u'Andrew Keegan', u'John Bradley', u'Jack Moore', u'Pat Skipper', u'John McLaughlin', u'Andrew Warne', u'Michael Winther', u'Malcolm Danare', u'Frank Novak', u'Kimberly Beck', u'Mirron E. Willis', u'John Storey', u'Robert Pine', u'Vanessa J. Wells', u'Giuseppe Andrews', u'Adam Tomei', u'Randy Oglesby', u'Nelson Mashita', u'Sharon Tay', u'Robin Groth', u'John Capodice', u'Eric Neal Newman', u'Kristof Konrad', u'Leland Orser', u'Jeff Goldblum', u'Frank Welker', u'Ross Elliot Bagley', u'James Wong', u'Lisa Star', u'Peter Jozef Lucas', u'Lee Strauss', u'Mae Whitman', u'Adam Baldwin', u'John Bennett Perry', u'Eric Michael Zee', u'Carlos La Camara'])

```

##Setup
This application stores the movie and actors locally in a mysql database. It checks this database first to only query the api when that film has no data locally.
This will require you to have MySQL running locally
I set it up as follows on ubuntu with the help of this useful tutorial http://zetcode.com/db/mysqlpython/

```sh
$ sudo apt-get install mysql-server
$ sudo apt-get install python-mysqldb
```

Login to MySQL as root and I created a database called testdb, a user called testuser and granted all on testdb to that user

```sh
mysql> CREATE DATABASE testdb;
mysql> CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test623';
mysql> USE testdb;
mysql> GRANT ALL ON testdb.* TO 'testuser'@'localhost';
mysql> quit;
```
This user is then referenced in the connection objects in the python scripts.

Interestingly using this MySQL backend we can now query that directly so I have also put up a SQL file of queries that could be interesting.


I also uploaded a text file of movies I scraped off IMDB which can be used to populate the database or for inspiration. 





