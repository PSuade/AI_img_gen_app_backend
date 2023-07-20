DROP TABLE IF EXISTS users;

CREATE TABLE users(
   ID INT PRIMARY NOT NULL,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   email TEXT UNIQUE NOT NULL,
   password  TEXT NOT NULL,
);