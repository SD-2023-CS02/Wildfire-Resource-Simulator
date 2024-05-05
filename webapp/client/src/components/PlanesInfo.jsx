import React from 'react';
import "../styles/planes-info.css";
import LAT from "../images/LAT.jpg";
import VLAT from "../images/VLAT.jpg";
import TankerBase from "../images/tanker_base.jpg";

class PlanesInfo extends React.Component {
    render() {
        return (
            <div className="planes-row">
                <h1 className="planes-title">Besides Wildfires, What are We Tracking?</h1>
                <div className="planes-info">
                    <div id="subsection-one">
                        <img className="planes-image" src={LAT} alt="LAT"/>
                        <h3>
                            Large Air Tankers (LATs)
                        </h3>
                        <p className="planes-description">
                            Large Air Tankers (LATs) play a vital role in wildfire combat, dispersing significant amounts of fire retardant to slow fire spread.
                            They support ground crews by establishing containment lines.
                            LATs, often retired commercial aircraft, efficiently cover moderate to large fire areas,
                            aiding in suppression efforts with their considerable capacity allowing LATs to deliver up to 4,000 gallons of fire retardant at a time.
                        </p>
                    </div>
                    <div id="subsection-two">
                        <img className="planes-image" src={VLAT} alt="VLAT"/>
                        <h3>
                            Very Large Air Tankers (VLATs)
                        </h3>
                        <p className="planes-description">
                            Very Large Air Tankers (VLATs) are pivotal in wildfire suppression, capable of carrying and dropping large volumes of fire retardant exceeding 9,000 gallons.
                            They establish fire lines, slowing down the spread, aiding ground crews.
                            VLATs, repurposed from commercial jets, efficiently cover vast areas, mitigating severe wildfires with their substantial retardant capacity.
                        </p>
                    </div>
                    <div id="subsection-three">
                        <img className="planes-image" src={TankerBase} alt="Tanker Bases"/>
                        <h3>
                            Tanker Bases
                        </h3>
                        <p className="planes-description">
                            Tanker bases serve as crucial hubs for aerial firefighting operations, strategically positioned across the
                            United States. These bases facilitate rapid deployment of firefighting aircraft for retardant loading and refueling.
                            With over one hundred bases nationwide, they ensure efficient coverage and support for firefighting efforts in different
                            regions during wildfire seasons.
                        </p>
                    </div>
                </div>
            </div>
        )
    }
}

export default PlanesInfo;