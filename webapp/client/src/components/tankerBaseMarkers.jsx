/**
 * Author: Kevin Dang
 * Date: 21 February 2024
 * Desc: A Marker componenet to display the tanker bases onto google maps
 * 
 * Last Updated: 5 April 2024
 */

import { Marker } from "@react-google-maps/api"
import Axios from "axios"
import { useEffect, useState } from "react"

export default function TankerBaseMarkers({ startDate, endDate, query, hideIcon, updateInfoBox }) {
    const [baseMarkers, setBaseMarkers] = useState([])

    // Fetch tanker base points
    useEffect(() => {
        Axios.get(process.env.REACT_APP_TANKER_BASE)
            .then(response => setBaseMarkers(response.data))
            .catch(error => console.log(error))
    }, [query === true])

    return (
        <>
            {!hideIcon && baseMarkers.map(baseMarker => (
                <Marker 
                    key={baseMarker.id}
                    position={{ lat: baseMarker.lat, lng: baseMarker.long }}
                    title={baseMarker.title}
                    icon={{
                        url: require('./../svg/airport-control-tower.svg').default,
                        strokeColor: '#006600',
                        fillColor: '#006600',
                        fillOpacity: 0.8,
                        scaledSize: new window.google.maps.Size(45, 45)
                    }}
                    onClick={() => {updateInfoBox(baseMarker)}}
                />
            ))}
        </>
    )
}