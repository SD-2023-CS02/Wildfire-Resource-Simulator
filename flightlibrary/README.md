# Flight Library

## What is this?
The Flight Data Library was created to quickly and easily gather all the flight data between 2 date points of a given list of tail numbers from FlightAware's AeroAPI. This entire library was built to ensure costs do not go over a desired amount because the data that will be getting requested programatically is not free. This data seamlessly grabs all the Flight ID's for each plane, then gathers all the location data for those flights and puts all the resulting data into 3 files.

## How to use it?

### API Key
To get an API Key for this data, the first step is to navigate to https://www.flightaware.com/ and create an account. Once an account is created you now have access to the developer tools. At the top right of the webpage you will navigate to "My AeroAPI" and select "API Keys". Here you can go through the process to Add API Key by clicking the button. Ensure that the API Key is at least a Standard Tier. A personal Tier will not allow you to query historical data which this library is created to use. Once the API key is generated it can be added into the config.py file.

### config.py
This file is built to allow you to have control over any mutatible values in the library. 

### Running
