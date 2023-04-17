from db.run_sql import run_sql

from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO country (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return(country)

def delete_all():
    sql = "DELETE FROM country"
    run_sql(sql)

def select_all():
    countries = []
    sql = "SELECT * FROM country"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'],row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM country WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['id'])
    return country

def select_by_name(name):
    country = None
    sql = "SELECT * FROM country WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['id'])
    return country

def delete(id):
    sql = "DELETE FROM city WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def cities(country):
    cities = []
    sql = "SELECT * FROM country WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row["name"], country, row["completed"], row["id"])
        cities.append(city)
    return cities