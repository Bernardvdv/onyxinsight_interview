# Django Interview Question

In this task you will write a small Django API from which numerical data read from sensors placed on a Wind Turbine can be retrieved or stored.

The requirements are:

* Create a model and API (at `/api/sensor`) to represent a "sensor". You should be able to create sensors at the end point with a payload like `'{"name": "Main Bearing Temperature", "unit": "Celcius"}'`. Sensor names should be unique. You should be able to retrieve information about a specific sensor at `/api/sensor/<sensor_id>` and a list of all of the sensors at `/api/sensor/`.
* Create an API endpoint to store data at /api/data/ which you can store and retrieve floating point numerical measurements from sensors.
  * You should be able to POST at the end point and create records. The payload for such a request should look like `'{"date": "2022-04-27 12:13", "sensor": "Main Bearing Temperature", "value": 12.0"}'`. You can assume that all values are floating point numbers.
  * You should support GET, POST and PATCH operations on the end point only.
  * You should be able to retrieve all records for a particular sensor at for e.g. `/api/data?sensor="Main+Bearing+Temperature"`
