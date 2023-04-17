from db.run_sql import run_sql

from models.city import City

from repositories import country_repository

def save(city):
    sql = "INSERT INTO city (name, country_id, completed) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return(city)

def delete_all():
    sql = "DELETE FROM city"
    run_sql(sql)

def select_all():
    cities = []
    sql = "SELECT * FROM city"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['completed'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM city WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result["country_id"])
        city = City(result["name"], country, result["completed"], result["id"])
    return city

def delete(id):
    sql = "DELETE FROM city WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE city SET (name, country_id, completed) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.completed, city.id]
    run_sql(sql, values)