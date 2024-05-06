# Flight Library

## What is this?
The Flight Data Library was created to quickly and easily gather all the flight data between 2 date points of a given list of tail numbers from FlightAware's AeroAPI. This entire library was built to ensure costs do not go over a desired amount because the data that will be getting requested programatically is not free. This data seamlessly grabs all the Flight ID's for each plane, then gathers all the location data for those flights and puts all the resulting data into 3 files.

## How to use it?

### API Key
To get an API Key for this data, the first step is to navigate to https://www.flightaware.com/ and create an account. Once an account is created you now have access to the developer tools. At the top right of the webpage you will navigate to "My AeroAPI" and select "API Keys". Here you can go through the process to Add API Key by clicking the button. Ensure that the API Key is at least a Standard Tier. A personal Tier will not allow you to query historical data which this library is created to use. Once the API key is generated it can be added into the config.py file.

### config.py
This file is built to allow you to have control over any mutatible values in the library. There are many values in this configuration file that can be edited to change how the program works.
APIKey - This is a required field for the library to function, the API Key needs to also be valid

##### Dates
  - These date values can be changed to adjust where the library queries as the start and ending years. 
  WARNING: Do not let the ending years go beyond the current date or it will spend extra money querying for dates that don't exist yet.

##### Threshold
  - This is the value that the program will quit at if it reaches this in cost. The default value set is $1200. It is in a double value, and can handle decimals and will not spend more money over the mark. 
  WARNING: the program will quit at the exact place that the threshold hits. will need physical adjustment by you to change where it starts on the next run if it did not complete running all the data. or it will just run from the start again

Files - Each of these is the file name and location that each piece of the data will either be pulled from or created into. The only file that needs to exist before run is the PLANE_ID_CSV full of just tanker tail numbers.

### Running
Running this library is very easy in any python development environment. I used PyCharm to create and run this code, it makes creating a python machine easy, and will run the code quickly after instalation of the required libraries.

## Costs

### Plane ID Retrival
To get a plane ID retrival, we get all flights in a weeks long incrament, and it costs $0.20 for a single weeks result set.

### Plane Route Retrival
To get a planes route, it takes a single flight_id from the Plane ID List created in the previous step and requests is track. This costs $0.06 for the single track.
