import React from 'react';
import "../styles/overview.css";

class Overview extends React.Component {
    render() {
        return (
            <div className="overview-row">
                <h1 className="overview-title">What is Our Project About?</h1>
                <div className="overview-content">
                    <p className="overview-description">
                        The current wildfire management strategy in the United States faces scrutiny due to inefficiencies in aerial firefighting resource allocation.
                        Fire Armada addresses this by raising awareness and advocating for change. 
                        Utilizing data-driven simulations and visual analytics, we highlight deficiencies in existing methods, focusing on large air
                        tankers (LATs) and very large air tankers (VLATs) due to their reliability and capacity. With wildfires exacerbated by climate change and poor forest management,
                        aerial retardant drops play a vital role in suppression efforts. LATs and VLATs are crucial assets, deployed from over one hundred strategically located tanker bases
                        across the country. Our project centers on analyzing flight trajectories and tanker base usage to identify operational inefficiencies.
                        Our simulator integrates wildfire data, flight trajectories of LATs and VLATs, and tanker base locations. Statistical analyses aim to uncover trends and inefficiencies, such as suboptimal base utilization and response times. We investigate whether increased drops or earlier responses reduce fire impact and assess plane usage efficiency.
                        Fire Armada seeks to drive change by advocating for improved resource allocation and management.
                        This may entail increased government support for private contractors, fleet expansion, enhanced detection methods, or better base and aircraft utilization. By promoting awareness and reform, we aim to enhance wildfire management for public safety and environmental conservation.
                    </p>
                    <video className="overview-video" src="https://video.wixstatic.com/video/30db8f_571763b4c89545ac8a353c7b5883bbab/1080p/mp4/file.mp4" preload="none" autoPlay loop playsInline muted></video>
                </div>
            </div>  
        )
    }
}

export default Overview;