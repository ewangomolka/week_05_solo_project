DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255),
    name VARCHAR(255),
    completed BOOLEAN,
    user_id INT NOT NULL REFERENCES users[id]
);