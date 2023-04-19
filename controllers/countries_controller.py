from flask import Blueprint, render_template, redirect, request
from repositories import country_repository, city_repository
from models.city import City
from models.country import Country

country_blueprint = Blueprint("country", __name__)

#NEW
#GET /all_destinations/new
@country_blueprint.route("/destinations/new")
def new_trip():
    country = country_repository.select_all()
    return render_template("destinations/new.html", all_countries=country)

#CREATE
#POST 
@country_blueprint.route("/destinations/new", methods=['POST'])
def create_country():
    print("hello")
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect("/countries")

#SHOW
#GET /countries/
@country_blueprint.route("/countries")
def show_countries():
    countries = country_repository.select_all()
    return render_template("destinations/countries.html", countries=countries)

#SHOW
#GET /countries/<id>
@country_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    return render_template("destinations/show_country.html", country=country)

#DELETE
#POST 
@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")

#EDIT_COUNTRY
#GET /destinations/<id>/edit
@country_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country= country_repository.select(id)
    return render_template("/destinations/edit_country.html", country=country)

#UPDATE
#PUT (POST) /destinations/<id>
@country_blueprint.route("/countries/<id>/edit", methods=['POST'])
def edit_country2(id):
    name = request.form['name']
    country = country_repository.select(id)
    country.name = name
    country_repository.update(country)
    return redirect("/countries/" + id )