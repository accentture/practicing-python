CREATE DATABASE IF NOT EXISTS master_python; /* CREATE A DATA BASE IN NOT EXISTS */

/* to create the database to able to create tables */
use master_python;

/* this project will has two tables: 
    the first table is for users
    the second table is for notes */
/* creating the first table */
CREATE TABLE users( /* in this part will be the differents fields  */
id          int(25) auto_increment not null, # it will autoincrement by every user added
                              # not null : it means that this field cannot be empty
names       varchar(100),
surnames    varchar(255),
email       varchar(255) not null,
password    varchar(255) not null,
fecha       date not null,      

/* creating constraint of the table, that is to say:
    --what is the primary key
    --what is the table identifier
    --what is the unique field , that is to say what is value that cannot be repeated in more cases (in more table registers)
 */
            /* these names is wrote by convention, I can use whatever name */
CONSTRAINT  pk_user PRIMARY KEY(id), /* primary key */
CONSTRAINT  uq_email UNIQUE(email) /* unique field, it cannot be repeated in the differents registers that the table has got */
)ENGINE = InnoDb; /* it means that will keep the referencial identidy  and all of kind of relations beetwen differents tables */


CREATE TABLE notes(
id          int(25) auto_increment not null ,
user_id     int(25) not null, /* this column is to relationate with the user table and can identify what notes is for every user */
title       varchar(255) not null,
description MEDIUMTEXT, /* MEDIUMTEXT : it allows to have many dates in a text */
fecha       date not null,

CONSTRAINT pk_notes PRIMARY KEY(id),
                                                # users table   #id field
CONSTRAINT fk_notes_user FOREIGN KEY(user_id) REFERENCES users (id)   #doing the relation with users table
    #FOREING KEY() : relationate user_id with users table and id field
/* min 7:30 */
)ENGINE = InnoDb;


/* 
    --finally to execute this code, copy and paste this code in MySQL
    --to press continue
    --finallly the table will be created
    --press structures to check my new tables
    --the gray key show relation with the other table
 */