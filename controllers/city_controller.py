from flask import Blueprint, render_template, request, redirect
from repositories import country_repository, city_repository
from models.city import City

city_blueprint = Blueprint("city", __name__)

#HOME
#GET /home
@city_blueprint.route("/home")
def home():
    return render_template("/home/home.html")
#INDEX
#GET /all_destinations
@city_blueprint.route("/all_destinations")
def all_destinations():
    all_destinations = city_repository.select_all()
    return render_template("all_destinations/index.html", all_destinations=all_destinations)
#SHOW
#GET /all_destinations/<id>
@city_blueprint.route("/all_destinations/<id>")
def show_city(id):
    city = city_repository.select(id)
    return render_template("all_destinations/show_city.html", city=city)
#SHOW
#GET /all_destinations/country/<id>
@city_blueprint.route("/all_destinations/country/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template("all_destinations/show_country.html", country=country)
#SHOW 
# GET /all_destinations/completed
@city_blueprint.route("/all_destinations/completed")
def show_completed(completed):
    all_completed = city_repository.select(completed)
    return render_template("all_destinations/show_completed.html", all_completed=all_completed)
#SHOW
#GET /all_destinations/to-do
@city_blueprint.route("/all_destinations/to-do")
def show_uncompleted(completed):
    all_completed = city_repository.select(completed)
    return render_template("all_destinations/to-do.html", all_completed=all_completed)
#EDIT
#GET /all_destinations/<id>/edit
@city_blueprint.route("/all_destinations/<id>/edit")
def edit_trip(id):
    city = city_repository.select(id)
    country = country_repository.select_all()
    return render_template("all_destinations/edit.html", city=city, all_countries=country)
#CREATE
#POST /all_destinations
@city_blueprint.route("/all_destinations", methods=['POST'])
def create_trip():
    name = request.form['name']
    country_id = request.form['country_id']
    completed = request.form['completed']
    country = country_repository.select(country_id)
    city = City(name, country, completed)
    city_repository.save(city)
    return redirect("/all_destinations")
#DELETE
#POST /all_destinations/<id>/delete
@city_blueprint.route("/all_destinations/<id>/delete", methods=['POST'])
def delete_trip(id):
    city_repository.delete(id)
    return redirect("/all_destinations")
#NEW
#GET /all_destinations/new
@city_blueprint.route("/all_destinations/new")
def new_trip():
    country = country_repository.select_all()
    return render_template("all_destinations/new.html", all_countries=country)
