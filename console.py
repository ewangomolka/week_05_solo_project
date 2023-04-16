from repositories import country_repository
from repositories import city_repository

from models.country import Country
from models.city import City

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Germany")
country_repository.save(country_1)

country_2 = Country("Monte Carlo")
country_repository.save(country_2)

country_3 = Country("Mexico")
country_repository.save(country_3)

country_4 = Country("Cuba")
country_repository.save(country_4)

country_5 = Country("Italy")
country_repository.save(country_5)

country_6 = Country("Nigeria")
country_repository.save(country_6)

city_1 = City("Eichenwalde", country_1, False)
city_repository.save(city_1)

city_2 = City("Monaco", country_2, False)
city_repository.save(city_2)

city_3 = City("Dorado", country_3, True)
city_repository.save(city_3)

city_4 = City("Havana", country_4, True)
city_repository.save(city_4)

city_5 = City("Rialto", country_5, False)
city_repository.save(city_5)

city_6 = City("Colosseo", country_5, False)
city_repository.save(city_6)

city_7 = City("Numbani", country_6, False)
city_repository.save(city_7)

city_repository.select_all()
country_repository.select_all()