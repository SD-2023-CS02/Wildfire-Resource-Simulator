import React from 'react';
import "../styles/dashboard.css";
import AcresBurnedGauge from "../images/gauges.png";
import PlaneContractors from "../images/contractors.png";
import Drops from "../images/drops.png";
import Suppression from "../images/suppression.png";
import VisitedBases from "../images/visited_bases.png";
import Airborne from "../images/airborne.png";
import Grounded from "../images/grounded.png";
import Response from "../images/response_time.png";
import Proximity from "../images/proximity.png";

class Dashboard extends React.Component {
    render() {
        return(
        <div className="dashboard">
            <div className="dashboard-row">
                <div className="dashboard-info">
                    <h2 className="dashboard-title">
                        Why Private Contractors?
                    </h2>
                    <p className="dashboard-description">
                        The use of privately owned Large Air Tankers (LATs) and Very Large Air Tankers (VLATs) by the United States is primarily due to the unique dynamics of firefighting operations and the cost-effectiveness associated with utilizing private contractors.
                        Private companies can rapidly mobilize their aircraft in response to wildfires. They can deploy their resources across different regions as needed, ensuring a quicker response time compared to waiting for government-owned assets, which might be limited in number and availability.
                        The involvement of private companies fosters innovation and competition in the aerial firefighting industry. Different companies may develop and employ new technologies or techniques, ultimately benefiting firefighting efforts.
                        While government agencies like the U.S. Forest Service and state firefighting agencies maintain their own firefighting resources, including aircraft, the addition of privately owned assets supplements these resources, providing additional capacity during periods of high fire activity or when government-owned assets are stretched thin.
                    </p>
                </div>

                <div className="dashboard-info">
                    <h2 className="visualization-title">Number of Tracked Tankers Grouped By Contractor</h2>
                    <img className="graph-contractors" src={PlaneContractors} alt="Missing Bar Chart"/>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="dashboard-info">
                    <h2 className="visualization-title">Fires Grouped by Acres Burned</h2>
                    <img className="graph-gauge" src={AcresBurnedGauge} alt="Missing Gauge Chart"/>
                </div>

                <div className="dashboard-info">
                    <h2 className="dashboard-title">
                        How Big are the Fires?
                    </h2>
                    <p className="dashboard-description">
                        We collected data pertaining to wildfires that occurred in the United States from 2020 through 2022.
                        The chart on the left takes all recorded fires during this time period and divides them into six groups distinguished by the amount of acres a given fire burned.
                        A total of 26 fires managed to burn over 50,000 acres, with one of the biggest being the Dixie Fire in California which
                        managed to burn over 400,000 acres in total. While catastrophically large fires occur like this in the U.S., the majority
                        of fires that took place from 2020 through 2022 managed to burn between 1 and 25 acres.

                    </p>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="big-info">
                    <h2 className="visualization-title">15 Most Visited Tanker Bases</h2>
                    <img className="graph-gauge" src={VisitedBases} alt="Missing Gauge Chart"/>
                    <p className="big-description">
                        Gateway is the most utilized tanker base, with over 1500 recorded visits from 2020 through 2022. This base likely plays a crucial role in firefighting efforts, given its high frequency of use.
                        On the other end of the spectrum, Tanacross has seen only one recorded visit during the same period. This suggests that it is the least utilized base for tracked air tankers.
                        Overall, the data indicates significant variation in utilization across different bases. This suggests that resources may be more effectively allocated to the bases that receive more visits,
                        and it may point to places for new bases to be considered or for old ones to be retired if those resources are needed elsewhere.
                    </p>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="dashboard-info">
                    <h2 className="dashboard-title">
                        Air Tanker Effectiveness
                    </h2>
                    <p className="dashboard-description">
                        We calculated the number of larger fires that received retardant drops from LATs and VLATs during 2020 through 2022.
                        Our data was limited due to missing information in the fire dataset, but of the instances with all necessary information,
                        only 39 fires received drops, while 230 did not. The suppression results (based on time and acres burned) for both groups of fires-those
                        that did and those that did not receive drops-was about % While it is possible that the similarities in average suppression results indicate that aerial
                        firefighting does not impact the outcome of a fire, we believe it may also be because the fires that received drops were worse and would have had a worse
                        average suppression result had they not received drops. It is also possible that our results may be skewed by the portion of fires we were not able to calculate
                        suppression results for due to missing data in our datasets.
                    </p>
                </div>

                <div className="dashboard-info">
                    <h2 className="visualization-title">Number of Fires Greater Than 500 Acres Receiving Attention from Tracked Tankers</h2>
                    <img className="graph-suppression" src={Drops} alt="Missing Bar Chart"/>
                    <h2 className="visualization-title">Average Suppression Results of Fires Greater Than 500 Acres Receiving Attention from Tracked Tankers</h2>
                    <img className="graph-suppression" src={Suppression} alt="Missing Bar Chart"/>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="big-info">
                    <h2 className="visualization-title">Average Flight Hours per Tanker per Month</h2>
                    <img className="graph-gauge" src={Airborne} alt="Missing Gauge Chart"/>
                    <p className="big-description">
                        The graph shows monthly average hours for LATs and VLATs for 2020-2022. Each LAT and VLAT is uniquely color-coded, and the
                        graph reveals the expected pattern of more usage during the summer months, especially July and August when fire season is at its peak.
                        Some planes are evidently used more during some times of the year than others, which is an unexpected pattern that may warrant further
                        investigation to see if all planes are being used efficiently.
                    </p>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="big-info">
                    <h2 className="visualization-title">Average Response Time per Aircraft compared to Suppression Results</h2>
                    <img className="graph-gauge" src={Response} alt="Missing Gauge Chart"/>
                    <p className="big-description">
                        Here we present the suppression result of each fire (as a percentage suppressed) plotted against the response time in hours. This statistic investigates a potential inefficiency
                        in which quicker response times would result in better suppression of fires. We did not, however, find any strong pattern suggesting that this is the case; suppression results are
                        fairly well distributed by response time. You may notice a collection of data points at 839 hours. This is due to an error for response times greater than 35 days. All dates greater
                        than 35 days have been truncated to fit on the graph, which will be changed in a future version.
                    </p>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="big-info">
                    <h2 className="visualization-title">Difference Grounded vs Airborne per Aircraft</h2>
                    <img className="graph-gauge" src={Grounded} alt="Missing Gauge Chart"/>
                    <p className="big-description">
                        This graph measures the average difference between the amount of time each aircraft spent on the ground vs in the air from 2020 through 2022.
                        Each craft is categorized by their tail number. If a given value for a plane is positive on the Y axis,
                        it means that aircraft spent more time in the air that year than usual. If it is negative, that craft was grounded more often than it was in the air.
                    </p>
                </div>
            </div>

            <div className="dashboard-row">
                <div className="big-info">
                    <h2 className="visualization-title">Proximity of Fires to Tanker Bases</h2>
                    <img className="graph-gauge" src={Proximity} alt="Missing Gauge Chart"/>
                    <p className="big-description">
                        We wondered if perhaps some tanker bases tended to be better located, generally closer to fires.
                        In order to explore this, we found the closest tanker base to each fire in our database. We then averaged the distances between
                        the base and the fire of all fires closest to a given base. In this way, we can see that some tanker bases are generally much closer to
                        fires—as close on average as 16.8 miles—while a few tend to be alarmingly far away—as far on average as 584 miles. This points to tanker
                        bases that should be relocated or areas that might benefit from a higher density of bases.
                    </p>
                </div>
            </div>
        </div>
        )
    }
}

export default Dashboard;
