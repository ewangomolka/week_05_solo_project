DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS country;

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    completed BOOLEAN,
    country_id INT NOT NULL REFERENCES country[id]
);