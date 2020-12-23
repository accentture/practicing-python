CREATE DATABASE IF NOT EXISTS personal_blog;

use personal_blog;

CREATE TABLE users(
    id          int(25) auto_increment not null,
    names       varchar(30),
    surnames    varchar(30),
    email       varchar(50) not null,
    password    varchar(30) not null,
    _date       date not null,

    CONSTRAINT pk_user PRIMARY KEY(id),
    CONSTRAINT uq_names UNIQUE(names),
    CONSTRAINT uq_surnames UNIQUE(surnames),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE = InnoDb;


CREATE TABLE programming(
    id          int(15) auto_increment not null,
    user_id     int(15) not null,
    topic       varchar(100) not null,
    description MEDIUMTEXT,
    _date       date not null,

    CONSTRAINT  pk_key PRIMARY KEY(id),
    CONSTRAINT  fk_programming_user FOREIGN KEY(user_id)REFERENCES users (id)

)ENGINE = InnoDb;


CREATE TABLE foods(
    id          int(15) auto_increment not null,
    user_id     int(15) not null,
    category    varchar(100) not null,
    name        varchar(100) not null,
    _date       date not null,

    CONSTRAINT  pk_key PRIMARY KEY(id),
    CONSTRAINT  pk_foods_user FOREIGN KEY(user_id) REFERENCES users (id)
)ENGINE = InnoDb;
