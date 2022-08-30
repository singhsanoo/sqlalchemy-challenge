# Surf’s Up 

## Backgroung

Climate analysis is perfromed on the area (Honolulu, Hawaii!). The following sections outlines the steps taken to accomplish this task.

### Part 1: Climate Analysis and Exploration

In this section, Python and SQLAlchemy is used to perform basic climate analysis and data exploration of the climate database. 

* [hawaii.sqlite](hawaii.sqlite) file is used to complete our climate analysis and data exploration.

* SQLAlchemy’s `create_engine` is used to connect to your SQLite database.

* SQLAlchemy’s `automap_base()` is used to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Python is linked to the database by creating a SQLAlchemy session.

#### Precipitation Analysis

* Performed an analysis of precipitation in the area.

* [starter notebook](climate.ipynb) includes the `date` vs `prcp`(precipitation) [plot](Images/precipitation.png). It also includes the summary statistic of precipitation data. 

#### Station Analysis

* Performed an analysis of stations in the area. For the most active station lowest, highest, and average temperatures are calculated using `func.min`, `func.max`, `func.avg`, and `func.count` in the queries

* [starter notebook](climate.ipynb) plots the results as a [histogram](Images/station-histogram.png) with `bins=12`, of the previous 12 months data of temperature observation data (TOBS), from the most active station. 

- - -

### Part 2: Climate App

Flask API is designed based on the queries that was developed in part1.

Flask is used to create the routes, different routes are as follows: [app.py](app.py)

* `/`

    * Homepage.

    * Lists all available routes.

* `/api/v1.0/precipitation`

    * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Returns the JSON representation of that dictionary.

* `/api/v1.0/stations`

    * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Returns a JSON list of temperature observations (TOBS) for the previous year of the most active station.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range (inclusive).


### Other Analyses

Below are some more queries that were attempted to answer few questions.

* Analysis data is provided in [temp_analysis_1.ipynb](temp_analysis_1.ipynb) and [temp_analysis_2.ipynb](temp_analysis_2.ipynb) notebooks.

#### Temperature Analysis 1

Hawaii is reputed to enjoy mild weather all year round. And, is there a meaningful difference between the temperatures in, for example, June and December?

* The average temperature in June at all stations across all available years in the dataset. And, the same for the temperature in December is calculated.

* Then the paired t-test is used to determine whether the difference in means, if any, is statistically significant.

#### Temperature Analysis 2

* Historical data in the dataset is used to find out what the temperature has previously been from August 1 to August 7.

* [temp_analysis_2.ipynb](temp_analysis_2.ipynb) has the [plot](Images/temperature.png) showing the minimum, average, and maximum temperature for matching dates from a previous year, as a bar chart

#### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates.

* [temp_analysis_2.ipynb](temp_analysis_2.ipynb) shows this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

* Calculated the daily normals for the previous year's matching dates. Normals are the averages for the minimum, average, and maximum temperatures.

* Plotted an area plot (`stacked=False`) for the [daily normals](Images/daily-normals.png).





