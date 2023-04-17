from flask import Blueprint, render_template, redirect, request
from repositories import country_repository, city_repository
from models.city import City
from models.country import Country

city_blueprint = Blueprint("city", __name__)

#HOME
#GET /home

@city_blueprint.route("/home")
def home():
    return render_template("/home.html")
#INDEX
#GET /all_destinations
@city_blueprint.route("/destinations")
def all_destinations():
    destinations = city_repository.select_all()
    print(len(destinations))
    return render_template("index.html", city_list=destinations)
#SHOW
#GET /all_destinations/<id>
@city_blueprint.route("/destinations/<id>")
def show_trip(id):
    city = city_repository.select(id)
    return render_template("destinations/show_trip.html", city=city)

#SHOW 
# GET /all_destinations/completed
@city_blueprint.route("/destinations/completed")
def show_completed():
    all_cities = city_repository.select_all()
    return render_template("destinations/show_completed.html", all_cities=all_cities)
#SHOW
#GET /all_destinations/to-do
@city_blueprint.route("/destinations/to-do")
def show_uncompleted():
    all_cities = city_repository.select_all()
    return render_template("destinations/to-do.html", all_cities=all_cities)
#EDIT
#GET /all_destinations/<id>/edit
@city_blueprint.route("/destinations/<id>", methods=['POST'])
def edit_trip(id):
    city = city_repository.select(id)
    city.mark_visited()
    city_repository.update(city)
    return redirect("/destinations/" + id)

#CREATE
#POST /all_destinations
@city_blueprint.route("/destinations", methods=['POST'])
def create_trip():
    print("hello")
    name = request.form['name']
    country_id = request.form['country_id']
    country = country_repository.select(country_id)
    city = City(name, country, completed=False)
    city_repository.save(city)
    return redirect("/destinations")

#DELETE
#POST /all_destinations/<id>/delete
@city_blueprint.route("/destinations/<id>/delete", methods=['POST'])
def delete_trip(id):
    city_repository.delete(id)
    return redirect("/destinations")
#NEW
#GET /all_destinations/new
@city_blueprint.route("/destinations/new")
def new_trip():
    country = country_repository.select_all()
    return render_template("destinations/new.html", all_countries=country)
