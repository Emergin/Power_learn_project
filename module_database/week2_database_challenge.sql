create database Movie;
use Movie;
DROP TABLE movies;

create table Actors(
id int auto_increment primary key,
name varchar(20) not null,
age int
);

create table Movies(
id int auto_increment primary key,
title varchar(20) not null,
year year
);