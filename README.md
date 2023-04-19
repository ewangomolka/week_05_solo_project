# week_05_solo_project
my week_05 solo project developing an app for a bucket list style destination tracker.
I have styled my specific app around the videogame Overwatch, in where heroes travel to different cities around the world saving the people from destruction.

Functionality/Brief
### MVP:

 * The app should allow the user to track countries and cities they want to visit and those they have visited.
 * The user should be able to create and edit countries
 * Each country should have one or more cities to visit
 * The user should be able to create and delete entries for cities
 * The app should allow the user to mark destinations as visited or still to see.
 
### EXTENSION (completed extensions):

 * Have separate pages for destinations visited and those still to visit.

### LANGUAGES USED:

 * Python3, HTML, CSS, PostgreSQL.

### HOW TO RUN:

 Once repository pulled, open integrated terminal:
 * dropdb travel_app
 * createdb travel_app
 * psql -d travel_app -f db/travel_app.sql
 * python3 console.py
 * python3 -m flask run
