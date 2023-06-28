drop database if exists people;

create database people;

use people;

create table user (
  id int auto_increment primary key,
  name varchar(50),
  place_of_birth varchar(50)
)