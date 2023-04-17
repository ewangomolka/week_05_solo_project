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

@country_blueprint.route("/destinations/new", methods=['POST'])
def create_country():
    print("hello")
    name = request.form['name']
    country = Country(name)
    country_repository.save(country)
    return redirect("/destinations/new")
