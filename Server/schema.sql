DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS calculations;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL
);

CREATE TABLE calculations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status TEXT NOT NULL,
  jobid TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);