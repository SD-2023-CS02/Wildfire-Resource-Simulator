const express = require('express')
const mysql2 = require('mysql2')
const mysqlPromise = require('mysql2/promise')
const createError = require('http-errors')
const sqlite3 = require('sqlite3')
const util = require('util')

/**
 * Format of config.json in root
 * 1. "host": "..."
 * 2. "database": "..."
 * 3. "user": "..."
 * 4. "password": "..."
 */
const credentials = require('../../config.json')

// setup express router
const router = express.Router()

router.post('/getFireLocationData', async (request, response, next) => {
    try {
        // refer to credentials for paramter format
        const connection = mysql2.createConnection(credentials)

        // fire data query to pull simple data from database
        const fireLocationQuery = 'SELECT * FROM FirePoint WHERE discovery_date BETWEEN (?) AND (?)'

        // run query to database
        connection.query(fireLocationQuery, [request.body.startDate, request.body.endDate], (error, rows, fields) => {
            // handle failed connections, failed queries
            if (error)
                next(createError.InternalServerError(error))

            let firePointList = []

            // check for empty/null query
            if (rows != undefined && rows != []) {
                for (const row of rows) {
                    firePointList.push({
                        id: row['fire_id'],
                        name: row['incident_name'],
                        gacc: row['gacc'],
                        initialAcres: row['initial_acres'],
                        finalAcres: row['incident_size_acres'],
                        discovered: row['discovery_date'],
                        control: row['control_date'],
                        contained: row['containment_date'],
                        fireout: row['fireout_date'],
                        date: row['create_date'],
                        lat: Number(row['latitude']),
                        long: Number(row['longitude'])
                    })
                }
            }

            // send query data to caller
            console.log(`Successful API call on endpoint /getFireLocationData`);
            response.send(firePointList)
        })
    }
    catch (error) {
        next(error)
    }
})

// GET Method to be used for Development Purposes only
router.post('/getLocalFireData', async (request, response, next) => {
    try {
        // Create connection to SQLite database
        const localDb = new sqlite3.Database('fire_data.db')

        // FirePoint SQL Query
        const fireQuery = 'SELECT * FROM FirePoint WHERE discovery_date BETWEEN (?) AND (?)' 

        localDb.all(fireQuery, [request.body.startDate, request.body.endDate], (error, rows) => {
            localDb.close()

            // check for errors, stop response if so
            if (error)
                return response.status(500).json({ error: error.message })

            console.log('Formatting Fire Points...')
            let firePointList = []

            if (rows != undefined && rows != []) {
                for (const row of rows) {
                    firePointList.push({
                        id: row['fire_id'],
                        name: row['incident_name'],
                        gacc: row['gacc'],
                        initialAcres: row['initial_acres'],
                        finalAcres: row['incident_size_acres'],
                        discovered: row['discovery_date'],
                        control: row['control_date'],
                        contained: row['containment_date'],
                        fireout: row['fireout_date'],
                        date: row['create_date'],
                        lat: Number(row['latitude']),
                        long: Number(row['longitude'])
                    })                
                }
            }

            response.send(firePointList)
        })
    } catch (error) {
        next(error)
    }
})

// Server-Based Tanker Base Endpoint
router.get('/getTankerBaseData', async (request, response, next) => {
    try {
        // Create connection and query
        const connection = mysql2.createConnection(credentials)
        const tankerBaseQuery = 'SELECT base_code, base_name, airport, region, elevation, latitude, longitude FROM TankerBase'

        connection.query(tankerBaseQuery, (error, rows, fields) => {
            // handle failed connection/query
            if (error)
                next(createError.InternalServerError(error))

            let tankerBases = []

            if (rows != undefined && rows != []) {
                for (const row of rows) {
                    tankerBases.push({
                        baseCode: row['base_code'],
                        baseName: row['base_name'],
                        airport: row['airport'],
                        region: row['region'],
                        elevation: row['elevation'],
                        lat: Number(row['latitude']),
                        long: Number(row['longitude'])
                    })
                }
            }

            // operation successful, send data
            console.log('Successful API call on endpoint /getTankerBaseData')
            response.send(tankerBases)
        })
    } catch(error) {
        next(error)
    }
})

// Local Tanker Base Endpoint
router.get('/getLocalTankerBaseData', async (request, response, next) => {
    try {
        // Create connection and query to local db
        const localDb = new sqlite3.Database('tankerBase_data.db')
        const tankerBaseQuery = 'SELECT base_code, base_name, airport, region, elevation, latitude, longitude FROM TankerBase'

        localDb.all(tankerBaseQuery, [], (error, rows) => {
            localDb.close() // close off connection

            // check for errors, stop response if so
            if (error)
                return response.status(500).json({ error: error.message })

            const tankerBases = rows.map(base => {
                return {
                    baseCode: base['base_code'],
                    baseName: base['base_name'],
                    airport: base['airport'],
                    region: base['region'],
                    elevation: base['elevation'],
                    lat: Number(base['latitude']),
                    long: Number(base['longitude'])
                }
            })

            // operation successful, send data
            console.log('Successful API call on endpoint /getLocalTankerBaseData')
            response.send(tankerBases)
        })
    } catch(error) {
        next(error)
    }
})

// Server Flight Endpoint
router.post('/getFlightData', async (request, response, next) => {
    try {
        // handle date time formatting
        const startDateTime = request.body.startDate.split("T")
        const endDateTime = request.body.endDate.split("T")

        const connection = await mysqlPromise.createConnection(credentials)

        // query all of the flight ids to grab per the date
        const flightIdQuery = 'SELECT DISTINCT flight_id FROM FlightInfo WHERE DATE(landing) >= DATE(?) AND DATE(takeoff) <= DATE(?)'

        // query for all flights / prepare for security?
        /**
         * Goal: Get Flights and all flights prior for set date
         * 
         * flight_id = 'flight-id-for-flight'
         * TIMESTAMP('YYYY-MM-DD hh:mm:ss') <- template for what input should be
         */
        const flightsQuery = 'SELECT * FROM Flight JOIN FlightInfo USING(flight_id) WHERE flight_id = ? AND flight_timestamp <= TIMESTAMP(?, ?) ORDER BY flight_timestamp DESC'

        // first query to get all flight_id's
        const [rows, fields] = await connection.execute(flightIdQuery, [startDateTime[0], endDateTime[0]]) // 0 = date in split
        const flight_ids = rows

        // get all flight data for the date provided
        const flightsPromise = flight_ids.map(async flight => {
            const [rows, fields] = await connection.execute(flightsQuery, [flight.flight_id, endDateTime[0], endDateTime[1]]) // 0 = Date, 1 = Time
            return rows.map(row => {
                return {
                    tail_no: row.tail_no,
                    flight_id: row.flight_id,
                    flight_timestamp: row.flight_timestamp,
                    lat: Number(row.latitude),
                    lng: Number(row.longitude),
                    altitude: Number(row.altitude),
                    altitudeChange: row.altitude_change,
                    groundSpeed: row.ground_speed,
                    heading: row.heading,
                    source: row.source,
                    destination: row.destination,
                    takeoff: row.takeoff,
                    landing: row.landing
                }
            })
        })

        // wait for queries to finish via Promise, remove any flights with no data
        let flights = await Promise.all(flightsPromise)
        
        // filter out flights with no data at the current time
        flights = flights.filter(rows => rows && rows.length > 0)

        console.log('Successful API call on endpoint /getFlightData')
        response.send(flights)
    } catch(error) {
        next(error)
    }
})

// Local Flight Endpoint 
router.post('/getLocalFlightData', async (request, response, next) => {
    try {
        // handle date time formatting
        const startDateTime = request.body.startDate.split("T")
        const endDateTime = request.body.endDate.split("T")

        const flightDb = new sqlite3.Database('flight_data.db')
        const flightDbAllPromise = util.promisify(flightDb.all).bind(flightDb)

        // query all of the flight ids to grab per the date
        const flightIdQuery = 'SELECT DISTINCT flight_id FROM FlightInfo WHERE DATE(landing) >= DATE(?) AND DATE(takeoff) <= DATE(?)'

        /**
         * Goal: Get Flights and all flights prior for set date
         * 
         * flight_id = 'flight-id-for-flight'
         * TIMESTAMP('YYYY-MM-DD hh:mm:ss') <- template for what input should be
         */
        const flightsQuery = 'SELECT * FROM Flight JOIN FlightInfo USING(flight_id) WHERE flight_id = ? AND flight_timestamp <= DATETIME(?, ?) ORDER BY flight_timestamp DESC'

        // first query to get all flight_id's
        const flightIds = await flightDbAllPromise(flightIdQuery, [startDateTime[0], endDateTime[0]])

        const flightsPromises = flightIds.map(async (flight) => {
            const rows = await flightDbAllPromise(flightsQuery, [flight.flight_id, endDateTime[0], endDateTime[1]])
            return rows.map(row => ({
                tail_no: row.tail_no,
                flight_id: row.flight_id,
                flight_timestamp: row.flight_timestamp,
                lat: Number(row.latitude),
                lng: Number(row.longitude),
                altitude: Number(row.altitude),
                altitudeChange: row.altitude_change,
                groundSpeed: row.ground_speed,
                heading: row.heading,
                source: row.source,
                destination: row.destination,
                takeoff: row.takeoff,
                landing: row.landing
            }))
        })

        // wait for all flight queries to finish
        const flights = await Promise.all(flightsPromises)

        // filter out flights with no data at the current time
        const filteredFlights = flights.filter(rows => rows && rows.length > 0)

        flightDb.close() // Close the database connection

        console.log('Successful API call on endpoint /getLocalFlightData')
        response.send(filteredFlights)
    } catch(error) {
        next(error)
    }
})

// Normal Plane Tail Numbers
router.get('/getTailNumbers', async (request, response, next) => {
    const tailNumberQuery = 'SELECT DISTINCT tail_no FROM Flight'

    try {
        const connection = await mysqlPromise.createConnection(credentials)

        // query for tail_no of Planes
        const [rows, fields] = await connection.execute(tailNumberQuery)

        console.log('Successful API call on endpoint /getTailNumbers')
        response.send(rows)
    } catch {
        next(error)
    }
})

// Local Plane Tail Numbers
router.get('/getLocalTailNumbers', async (request, response, next) => {
    const tailNumberQuery = 'SELECT DISTINCT tail_no FROM Flight'

    try {
        const flightDb = new sqlite3.Database('flight_data.db')
        flightDb.all(tailNumberQuery, [], (error, rows) => {
            flightDb.close()
            console.log('Successful API call on endpoint /getLocalTailNumbers')
            response.send(rows)
        })
    } catch {
        next(error)
    }
})

// retrieves aircraft specs regarding the tanker planes we intend to track
router.get('/getTankerData', async (request, response, next) => {
    try {
        // refer to credentials for paramter format
        const connection = mysql2.createConnection(credentials)

        const tankerQuery = 'SELECT * FROM AirTanker JOIN FirePlane USING (tanker_type)'

        connection.query(tankerQuery, (error, rows, fields) => {
            // handle failed connections, failed queries
            if (error)
                next(createError.InternalServerError(error))

            let tankerList = []

            // check for empty/null query
            if (rows != undefined && rows != []) {
                for (const row of rows) {
                    tankerList.push({
                        type: row['tanker_type'],
                        tank: Number(row['tank_size']),
                        id: row['tail_no'],
                        contractor: row['contractor']
                    })
                }
            }

            // send query data to caller
            console.log(`Successful API call on endpoint /getTankerData`);
            response.send(tankerList)
        })

    } catch (error) {
        next(error)
    }
})

// retrieves fire containment dates, fireout dates, fire size upon discovery, and incident size
router.get('/getFireContainmentData', async (request, response, next) => {
    try {
        // refer to credentials for paramter format
        const connection = mysql2.createConnection(credentials)

        const fireContainmentQuery = 'SELECT * FROM FirePoint WHERE YEAR(create_date) = \'2020\' and MONTH(create_date) = \'1\' and containment_date IS NOT NULL and fireout_date IS NOT NULL and discovery_acres IS NOT NULL and discovery_acres > 0.1 and incident_size_acres IS NOT NULL and incident_size_acres > 0.1'

        connection.query(fireContainmentQuery, (error, rows, fields) => {
            // handle failed connections, failed queries
            if (error)
                next(createError.InternalServerError(error))
            
            let fireContainmentList = []

            // check for empty/null
            if (rows != undefined && rows != []) {
                for (const row of rows) {
                    fireContainmentList.push({
                        containment: row['containment_date'],
                        fireout: row['fireout_date'],
                        discovery: row['discovery_acres'],
                        size: row['incident_size_acres']
                    })
                }
            }

            // send query data to caller
            console.log(`Successful API call on endpoint /getTankerData`);
            response.send(fireContainmentList)

        })

    } catch (error) {
        next(error)
    }
    
})

module.exports = router