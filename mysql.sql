CREATE DATABASE personas;
show databases;
create table usuarios(
id_usuarios int not null auto_increment,
nombre varchar(150) not null,
apellido varchar(150)not null,
edad int not null,
email varchar(200) not null,
primary key (id_usuarios)
);