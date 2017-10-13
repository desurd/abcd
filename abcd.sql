--------------------------
-- need to have postgresql 
-- installed on the server /
-- local machine


-- DATABASE CREATION
-- Database: tripbkdata
-- DROP DATABASE abcddata;
CREATE DATABASE abcddata
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       --LC_COLLATE = 'en_US.UTF-8'
       --LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;
COMMENT ON DATABASE abcddata
  IS 'automatic creation for abcd database and table';

------------------------------
-- CONNECTION TO THE DATABASE 
-- connection done by using psql commande
\c abcddata
--
--------------------------------
---- database schema definition
---- Schema: public
-- DROP SCHEMA public;
CREATE SCHEMA abcd
  AUTHORIZATION postgres;
GRANT ALL ON SCHEMA abcd TO postgres;
GRANT ALL ON SCHEMA abcd TO public;
COMMENT ON SCHEMA abcd
  IS 'standard public schema';

-- change public schema to abcd schema
SET SCHEMA 'abcd';

------ Table: abcd.users
---- DROP TABLE public.users;
DROP TABLE abcd.users;
---- CREATE TABLE public.users
CREATE TABLE abcd.users
(
  userid character(17) NOT NULL,
  username character(17),
  knickname character(10),
  password character(10)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE abcd.users
  OWNER TO postgres;


------------------------------------
---- Table: abcd.project
DROP TABLE abcd.projects;
CREATE TABLE abcd.projects
(
  id integer NOT NULL,
  projectname character(40),
  data character(40),   -- need to change as json data reference
  userid int ,
  CONSTRAINT projectid_pkey PRIMARY KEY (id)
  --CONSTRAINT fk_userid FOREIGN KEY (userid)
  --  REFERENCES abcd.users (userid) MATCH SIMPLE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE abcd.projects
  OWNER TO postgres;

---- Table: abcd.board
DROP TABLE abcd.board;
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


---- Table: abcd.board
DROP TABLE abcd.slices;
---- will contains the different
---- slices necessary to define the board
---- skeleton
CREATE TABLE abcd.slices
(
  sliceid integer NOT NULL,
  slicename character(20),
  dimensionb character(20),
  projectid int,
  CONSTRAINT sliceid_pkey PRIMARY KEY (sliceid)
  --CONSTRAINT fk_projectid FOREIGN KEY (projectid)
  -- REFERENCES abcd.projects (projectid) MATCH SIMPLE
)
WITH (
  OIDS=FALSE
);

------------------------------------
---- GRANT ACCESS to the different
---- users
---- user: postgres
--GRANT ALL ON TABLE abcd.boardid TO postgres;
--GRANT ALL ON TABLE abcd.boardtype TO postgres;
--GRANT ALL ON TABLE abcd.slicenb TO postgres;
--
---- user: abcdread
--GRANT SELECT ON TABLE abcd.boardid TO abcdread;
--GRANT SELECT ON TABLE abcd.boardtype TO abcdread;
--GRANT SELECT ON TABLE abcd.slicenb TO abcdread;
----
------ user: abcdwrite
--GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE abcd.boardid TO abcdwrite;
--GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE abcd.boardtype TO abcdwrite;
--GRANT SELECT, UPDATE, INSERT, DELETE ON TABLE abcd.slicenb TO abcdwrite;

-- user: lemonadmin
--GRANT ALL ON TABLE public.trip TO lemona;

