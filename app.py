import numpy as np
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine,reflect=True)

# Save references to each table
Station = Base.classes.station
Measurment = Base.classes.measurement


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():

    """List of available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    return( 'prcp' )

@app.route("/api/v1.0/stations")
def stat():
    return( 'stat' )

@app.route("/api/v1.0/tobs")
def temp():
    return( 'temp' )

@app.route("/api/v1.0/<start>")
def startDate(start):
    return( 'MN' )


@app.route("/api/v1.0/<start>/<end>")
def startEndDate(start,end):
    return( 'k' )


# @app.route("/")
# def welcome():
#     return (
#         f"Welcome to the Justice League API!<br/>"
#         f"Available Routes:<br/>"
#         f"/api/v1.0/justice-league<br/>"
#         f"/api/v1.0/justice-league/Arthur%20Curry<br/>"
#         f"/api/v1.0/justice-league/Bruce%20Wayne<br/>"
#         f"/api/v1.0/justice-league/Victor%20Stone<br/>"
#         f"/api/v1.0/justice-league/Barry%20Allen<br/>"
#         f"/api/v1.0/justice-league/Hal%20Jordan<br/>"
#         f"/api/v1.0/justice-league/Clark%20Kent/Kal-El<br/>"
#         f"/api/v1.0/justice-league/Princess%20Diana"
#     )


# @app.route("/api/v1.0/<start>/<end>")
# def justice_league_character(start,end):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     # canonicalized = real_name.replace(" ", "").lower()
#     # for character in justice_league_members:
#     #     search_term = character["real_name"].replace(" ", "").lower()

#     #     if search_term == canonicalized:
    # return jsonify('haracter')









if __name__ == "__main__":
    app.run(debug=True)

