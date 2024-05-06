const express = require('express')
const cors = require('cors')
const createError = require('http-errors')

// port set
const PORT = process.env.PORT || 8080

// Data endpoint connections - serveronly
const ApiRoutes = require('./Routes/API.route')

// setup express connections
const app = express()

// setup settings for express
app.use(express.urlencoded({ extended: false }))
app.use(express.json())
app.use(cors())

// Data Connections Routes
app.use('/api', ApiRoutes)

// Error Check on invalid route/errors
app.use(async (request, response, next) => {
    console.error('Invalid access to url path, ERROR likely', 404)
    next(createError.NotFound('This url path was not found'))
})

/*
json error message for client receiver if anything goes wrong
  - Most likely to happen with unknown routes or errors mid-handle on route
  - _ means unused required parameter
*/
app.use((error, request, response, next) => {
    response.status(error.status || 500)
    response.send({
        error: {
            status: error.status || 500,
            message: error.message
        }
    })
})

// allow express to listen for connections
app.listen(PORT, () => {
    console.log(`Express connection listening on localhost:${PORT}`)
})