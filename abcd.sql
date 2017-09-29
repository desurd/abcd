--------------------------
-- need to have postgresql 
-- installed on the server /
-- local machine


-- DATABASE CREATION
-- Database: tripbkdata
DROP DATABASE abcddata;
CREATE DATABASE abcddata
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;
COMMENT ON DATABASE tripbkdata
  IS 'automatic creation for abcd database and table';

------------------------------
-- CONNECTION TO THE DATABASE 
-- connection done by using psql commande
\c abcddata

------------------------------
-- database schema definition
-- Schema: public
DROP SCHEMA abcd;
CREATE SCHEMA abcd
  AUTHORIZATION postgres;
GRANT ALL ON SCHEMA abcd TO postgres;
GRANT ALL ON SCHEMA abcd TO public;
COMMENT ON SCHEMA public
  IS 'standard public schema';

-------------------------------
-- User definition
CREATE USER abcdadmin WITH PASSWORD 'shapeadmin';
CREATE USER abcdwrite WITH PASSWORD 'shapewrite';
CREATE USER abcdread WITH PASSWORD 'shaperead';

-- Table: abcd.users
-- DROP TABLE abcd.users;
CREATE TABLE abcd.users
(
  userid character(17) NOT NULL,
  user character(17),
  knickname character(10),
  password character(10),
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.users
  OWNER TO postgres;

----------------------------------
-- Table: abcd.project
-- DROP TABLE abcd.project;
CREATE TABLE abcd.project
(
  id integer NOT NULL,
  projectname character(40),
  data character(40),   -- need to change as json data reference
  userid int ,
  CONSTRAINT projectid_pkey PRIMARY KEY (id)
  CONSTRAINT fk_userid FOREIGN KEY (userid)
    REFERENCES abcd.users (userid) MATCH SIMPLE
)
WITH (
  OIDS=FALSE
);

ALTER TABLE abcd.project
  OWNER TO postgres;

-- Table: abcd.board
-- DROP TABLE abcd.board;
CREATE TABLE abcd.board
(
  boardid integer NOT NULL,
  boardtype character(20),
  slicenb int,
  CONSTRAINT boardid_pkey PRIMARY KEY (boardid)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE abcd.board
  OWNER TO postgres;


-- Table: abcd.board
-- DROP TABLE abcd.slice;
-- will contains the different
-- slices necessary to define the board 
-- skeleton
CREATE TABLE abcd.slice
(
  sliceid integer NOT NULL,
  slicename character(20),
  dimensionb character(20),
  projectid int,
  CONSTRAINT sliceid_pkey PRIMARY KEY (sliceid),
  CONSTRAINT fk_projectid FOREIGN KEY (projectid)
    REFERENCES abcd.project (projectid) MATCH SIMPLE
)



----------------------------------
-- GRANT ACCESS to the different
-- users
-- user: postgres
GRANT ALL ON TABLE public.cardef TO postgres;
GRANT ALL ON TABLE public.history TO postgres;
GRANT ALL ON TABLE public.trip TO postgres;

-- user: lemonread
GRANT SELECT ON TABLE public.cardef TO lemonr;
GRANT SELECT ON TABLE public.history TO lemonr;
GRANT SELECT ON TABLE public.trip TO lemonr;

-- user: lemonwrite
GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE public.cardef TO lemonw;
GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE public.history TO lemonw;
GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE public.trip TO lemonw;

-- user: lemonadmin
GRANT ALL ON TABLE public.trip TO lemona;

