/**
 * Author: Kevin Dang
 * Date: 21 February 2024
 * Desc: A Marker and Polyline component to display flights and their flight path. 
 * 
 * Last Updated: 5 April 2024
 */

import { Marker, Polyline } from "@react-google-maps/api"
import Axios from "axios"
import { useEffect, useState } from "react"
import { faPlaneUp } from "@fortawesome/free-solid-svg-icons"

export default function FlightPathMarkers({ startDate, endDate, query, hideIcon, setHideIcon, updateQuery, updateInfoBox }) {
    const [flights, setFlights] = useState([])
    const [coordinates, setCoordinates] = useState([])
    const [colors, setColors] = useState({})

    // handles the flight marker persistance problem
    const handleNewInfo = (position, id, tail, flightInfo) => {
        updateInfoBox({ 
            flight_id: id,
            source: flightInfo.source,
            destination: flightInfo.destination,
            takeoff: flightInfo.takeoff,
            landing: flightInfo.landing,
            lat: position.lat,
            long: position.lng,
            tail_no: tail 
        })
    }

    useEffect(() => {
        // check if in range
        if (startDate < '2020-01-01' || endDate > '2022-12-31') {
            console.log('Invalid Date Range')
            return
        }

        Axios.post(process.env.REACT_APP_FLIGHTS, {
            startDate: startDate,
            endDate: endDate
        }).then(response => {
            // set flights
            setFlights(response.data)

            // create coordiante path and numerics format
            const coordinatePath = response.data.map(flight => {
                // format polyline path
                return {
                    tail_no: flight[0].tail_no,
                    path: flight.map(coordinate => ({
                        lat: coordinate.lat,
                        lng: coordinate.lng
                    }))
                }
            })
            setCoordinates(coordinatePath)
            setHideIcon(false)
            updateQuery()
        })
        .catch(error => console.log(error))   
    }, [query === true])

    // generate a random color for every tail_number
    useEffect(() => {
        const hexCharacters = "0123456789ab"

        Axios.get(process.env.REACT_APP_TAIL_NUMBER)
        .then(response => {
            const colors = {}
            for(const index of response.data) {
                let hexColor = "#"
                for (let i = 0; i < 3; i++) {
                    if (i === 1) {
                        const randomIndex = Math.floor(Math.random() * Math.floor(hexCharacters.length / 2))
                        hexColor += hexCharacters[randomIndex]
                    } else {
                        const randomIndex = Math.floor(Math.random() * hexCharacters.length)
                        hexColor += hexCharacters[randomIndex]
                    }
                    for (const tail in colors) {
                        if (colors[tail] === hexColor) {
                            i = -1
                            console.log(`Duplicate Color Found: ${hexColor}`)
                            hexColor = "#"
                            break
                        }
                    }
                        
                }
                colors[index.tail_no] = hexColor
            }
            setColors(colors)
        })
    }, [])

    return (
        <>
            {/* FlightMarker */}
            {!hideIcon && flights.map((flight) => (
                <Marker 
                    key={flight[0].tail_no}
                    position={{ lat: flight[0].lat, lng: flight[0].lng }}
                    title={flight[0].tail_no}
                    icon={{
                            path: faPlaneUp.icon[4],
                            strokeColor: '#ffffff',
                            fillColor: colors[flight[0].tail_no],
                            anchor: new window.google.maps.Point(
                                faPlaneUp.icon[0] / 2, // width
                                faPlaneUp.icon[1] / 1.1, // height, connected mininally to flightPath
                            ),
                            fillOpacity: 1,
                            scale: 0.0575,
                            rotation: flight[0].heading
                    }}
                    onClick={() => {handleNewInfo({ 
                        lat: flight[0].lat + 0.2, 
                        lng: flight[0].lng 
                    }, 
                    flight[0].flight_id, 
                    flight[0].tail_no, 
                    { 
                        source: flight[0].source, 
                        dest: flight[0].destination, 
                        takeoff: flight[0].takeoff, 
                        landing: flight[0].landing 
                    })}}
                />
            ))}
            {/* FlightPathMarkers */}
            {coordinates.map((flightPath, index) => (
                <Polyline 
                    key={index}
                    path={flightPath.path}
                    geodesic={true}
                    options={{
                        strokeColor: colors[flightPath.tail_no],
                        strokeOpacity: 0.9,
                        strokeWeight: 3,
                        visible: !hideIcon
                    }}
                />
            ))}
        </>
    )
}