from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

city_repository.delete_all()
country_repository.delete_all()



country_repository.select_all()
city_repository.select_all()