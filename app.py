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
        f"/api/v1.0/YYYY-MM-DD     #start date<br/>"
        f"/api/v1.0/YYYY-MM-DD/YYYY-MM-DD    #start date/end date"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)
    results = session.query(Measurment.date, Measurment.prcp).all()

    session.close

    prcp_dict = {}
    for date, prcp in results:        
        prcp_dict[f'{date}'] = prcp

    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stat():
    session = Session(engine)
    results = session.query(Station.station).all()

    session.close

    station_list = list(np.ravel(results))

    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def temp():
    session = Session(engine)
    m_act_station = session.query(Measurment.station, func.count(Measurment.station). \
                    label('count')).group_by(Measurment.station).order_by(desc('count')).first()

    last_act_date = session.query(func.max(Measurment.date)).first()
    one_yr_date = dt.strptime(last_act_date[0], '%Y-%m-%d').date() - relativedelta(months=12)

    results = session.query(Measurment.date, Measurment.tobs).filter(Measurment.station == f'{m_act_station[0]}').filter(Measurment.date >= f'{one_yr_date}').all()

    session.close

    temp_list = []
    for date,temp in results:
        temp_list.append(temp)
    
    return jsonify(temp_list)


@app.route("/api/v1.0/<start>")
def startDate(start):
    session = Session(engine)
    tmin = session.query(func.min(Measurment.tobs)).filter(Measurment.date >= f'{start}').first()
    tmax = session.query(func.max(Measurment.tobs)).filter(Measurment.date >= f'{start}').first()
    tavg = session.query(func.avg(Measurment.tobs)).filter(Measurment.date >= f'{start}').first()

    session = Session(engine)

    return jsonify([f'minTemp = {tmin[0]}, maxTemp = {tmax[0]}, avgTemp = {round(tavg[0],2)}'])


@app.route("/api/v1.0/<start>/<end>")
def startEndDate(start,end):
    session = Session(engine)
    tmin = session.query(func.min(Measurment.tobs)).filter(Measurment.date >= f'{start}').filter(Measurment.date <= f'{end}').first()
    tmax = session.query(func.max(Measurment.tobs)).filter(Measurment.date >= f'{start}').filter(Measurment.date <= f'{end}').first()
    tavg = session.query(func.avg(Measurment.tobs)).filter(Measurment.date >= f'{start}').filter(Measurment.date <= f'{end}').first()

    session = Session(engine)

    return jsonify([f'minTemp = {tmin[0]}, maxTemp = {tmax[0]}, avgTemp = {round(tavg[0],2)}'])


if __name__ == "__main__":
    app.run(debug=True)

