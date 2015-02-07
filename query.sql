//SQL queries for taking a look at our local MySQL database

select ActorName, count(*) Films from FilmActors group by 1 having Films>1
order by 2 desc limit 100;

select FilmName,trim(FilmName),  from FilmActors 

create table FilmActors as
select Id, Timestamp as Timestamp, trim(FilmName) as FilmName, ActorName  from FilmActors2;
