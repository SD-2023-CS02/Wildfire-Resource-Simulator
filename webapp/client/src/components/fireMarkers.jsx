/* 
    Author: Kole Davis
    Date: 3 December 2023
    Desc.: This component of the webapp is designed to load fire location data from our server
    into plottable map coordinates that will then be loaded into the Google Maps API.

    Updated: 5 April 2024 by Kevin Dang
*/

import React, { useState, useEffect } from "react";
import { Marker } from "@react-google-maps/api";
import Axios from "axios";

const FireMarkers = ({ startDate, endDate, query, hideIcon, updateInfoBox }) => {
    const [markers, setMarkers] = useState([])

    // Fetches fire marker data stored on our server database
    useEffect(() => {
        // check if in range
        if (startDate < '2020-01-01' || endDate > '2022-12-31' || startDate > endDate) {
            console.log('Invalid Date Range')
            return
        }

        console.log('Running Fire Query')

        // query for FirePoint locations
        Axios.post(process.env.REACT_APP_FIRE_LOCATION, {
            startDate: startDate,
            endDate: endDate
        }).then((response) => {
            setMarkers(response.data)
        }).catch((error) => { // handle network, 404 errors
            console.log(error)
        })
    }, [query === true])

    // Will plot each marker when FireMarkers component is added to the map
    return (
        <>
            {!hideIcon && markers.map(marker => (
                <Marker
                    key={marker.id}
                    position={{ lat: marker.lat, lng: marker.long }}
                    title={marker.id}
                    icon={{
                        url: require('./../svg/fire-left.svg').default,
                        strokeColor: '#ffffff',
                        fillColor: '#440000',
                        fillOpacity: 1,
                        scaledSize: new window.google.maps.Size(30, 30)
                    }}
                    onClick={() => {updateInfoBox(marker)}}
                />
            ))}
        </>
    )
}

export default FireMarkers;

