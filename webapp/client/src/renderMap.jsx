import { GoogleMap, useLoadScript, InfoWindow } from "@react-google-maps/api";
import { useMemo, useState } from "react";
import "./renderMap.css";
import FireMarkers from "./components/fireMarkers";
import TankerBaseMarkers from "./components/tankerBaseMarkers";
import FlightPathMarkers from "./components/flightMarkers";
import Header from "./components/Header";
import Overview from "./components/Overview";
import PlanesInfo from "./components/PlanesInfo";
import Dashboard from "./components/Dashboard";


export const App = () => {
  const { isLoaded } = useLoadScript({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_API_KEY,
  });

  // date states
  const [startInputDate, setStartInputDate] = useState('2020-02-05T00:01')
  const [endInputDate, setEndInputDate] = useState('2020-02-06T13:00')
  const [query, setQuery] = useState(false)
  const [badQuery, setBadQuery] = useState(false)

  // hide icon states
  const [hideFires, setHideFires] = useState(false)
  const [hideBases, setHideBases] = useState(false)
  const [hideFlights, setHideFlights] = useState(false)

  // event invoked methods
  const setStartDate = (event) => setStartInputDate(event.target.value) 
  const setEndDate = (event) => setEndInputDate(event.target.value)
  const updateHideFlights = (value) => setHideFlights(value)
  const updateQuery = () => setQuery(false)

  // icon methods/states
  const [infoBox, setInfoBox] = useState(undefined)
  const updateInfoBox = (value) => {
    console.log(value)
    setInfoBox(value)
  }

  const validateQuery = () => {
    if (startInputDate < '2020-01-01' || endInputDate > '2022-12-31' || startInputDate > endInputDate) {
      setBadQuery(true)
      return
    }

    // dates are valid
    setQuery(true)
    setHideFlights(true)
    setBadQuery(false)
  }

  const center = useMemo(() => ({ lat: 47.658779, lng: -117.426048 }), []);

  return (
      <div className="wrapper">
        {/* Header Content */}
        <Header/>

        {/* Overview Content */}
        <Overview/>

        {/* Planes Info Content */}
        <PlanesInfo/>

        {/* Map-related Content */}
        <div className="map-slider-wrapper">
          <div className="map">
            {!isLoaded ? (
              <h1>Loading...</h1>
            ) : (
              <GoogleMap
                mapContainerClassName="google-container"
                center={center}
                zoom={4}
                options={{
                  streetViewControl: false,
                  mapTypeControl: false,
                  fullscreenControl: false
                }}
              >
                <FireMarkers startDate={startInputDate} endDate={endInputDate} query={query} hideIcon={hideFires} updateInfoBox={updateInfoBox} />
                <TankerBaseMarkers startDate={startInputDate} endDate={endInputDate} query={query} hideIcon={hideBases} updateInfoBox={updateInfoBox} />
                <FlightPathMarkers startDate={startInputDate} endDate={endInputDate} query={query} hideIcon={hideFlights} setHideIcon={updateHideFlights} updateQuery={updateQuery} updateInfoBox={updateInfoBox} />

                {
                  infoBox !== undefined ?  
                  <InfoWindow
                    position={{ lat: infoBox.lat + 0.2, lng: infoBox.long }}
                    onCloseClick={() => setInfoBox(undefined)}
                  >
                    {infoBox.tail_no ? <>
                        <h3>Aircraft: {infoBox.tail_no}</h3>
                        <p>Flight ID: {infoBox.flight_id}</p>
                        <p>Departing Airport: {infoBox.source || 'Unknown'}</p>
                        <p>Arriving Airport: {infoBox.destination || 'Unknown'}</p>
                        <p>Takeoff: {new Date(infoBox.takeoff).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.takeoff).toLocaleTimeString('en-US') || 'Unknown'}</p>
                        <p>Landing: {new Date(infoBox.landing).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.landing).toLocaleTimeString('en-US') || 'Unknown'}</p>
                      </> : (
                      infoBox.name ? <>
                        <h3>Incident: {infoBox.name}</h3>
                        <p>Fire Discovered on: {new Date(infoBox.discovered).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.discovered).toLocaleTimeString('en-US') || 'Unknown'}</p>
                        <p>Contained on: {new Date(infoBox.contained).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.contained).toLocaleTimeString('en-US') || 'Unknown'}</p>
                        <p>Declared Under Control on: {new Date(infoBox.control).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.control).toLocaleTimeString('en-US') || 'Unknown'}</p>
                        <p>Fire was put out on: {new Date(infoBox.fireout).toLocaleDateString('en-US') || 'Unknown'} : {new Date(infoBox.fireout).toLocaleTimeString('en-US') || 'Unknown'}</p>
                        <p>Initial acres burned: {infoBox.initialAcres || 'Unknown'}</p>
                        <p>Total acres burned: {infoBox.finalAcres || 'Unknown'}</p>
                        <p>GACC Region: {infoBox.gacc || 'Unknown'}</p>
                      </> : (
                      infoBox.baseName ? <>
                        <h3>Base: {infoBox.baseName}</h3>
                        <p>Airport: {infoBox.airport}</p>
                        <p>Region: {infoBox.region}</p>
                        <p>Elevation: {infoBox.elevation}</p>
                      </> : null
                        )
                      )
                    }
                  </InfoWindow>
                  : null
                }
                
              </GoogleMap>
            )}
          </div>

          <div className="slider">
            <div className="error">
              { 
                badQuery ? 
                <p id="error">Invalid Date Range. Valid Years are 2020-2022.</p> 
                : <p>Please Enter Valid Dates between 2020 and 2022</p>
              }
            </div>
            <div className="dates">
              <input type="datetime-local" name="Start Date" id="start" value={startInputDate} onChange={setStartDate} onClick={() => setBadQuery(false)} />
              <input type="datetime-local" name="End Date" id="end" value={endInputDate} onChange={setEndDate} onClick={() => setBadQuery(false)} />

              {/* Button to change the state of query to trigger requery for backend */}
              <input type="button" value="Search" onClick={() => validateQuery()} />
            </div>

            <div className="icon-hiders">
              {hideFires ? 
                <input type="button" value="Show Fires" onClick={() => {setHideFires(!hideFires)}} /> 
                : <input type="button" value="Hide Fires" onClick={() => {setHideFires(!hideFires)}} />}
              {hideBases ? 
                <input type="button" value="Show Tanker Bases" onClick={() => {setHideBases(!hideBases)}} /> 
                : <input type="button" value="Hide Tanker Bases" onClick={() => {setHideBases(!hideBases)}} />}
              {
                !query ? (
                  hideFlights ? 
                    <input type="button" value="Show Flights" onClick={() => {setHideFlights(!hideFlights)}} /> 
                    : <input type="button" value="Hide Flights" onClick={() => {setHideFlights(!hideFlights)}} />
                ) : null
              }
            </div>
            
          </div>
        </div>

        {/* Wildfire Statistics */}
        <div className="stats stats-fire"></div>

        {/* Plane Statistics */}
        <div className="stats stats-plane"></div>

        {/* Dashboard-related content */}
        <Dashboard/>

      </div>
  );
};

export default App;