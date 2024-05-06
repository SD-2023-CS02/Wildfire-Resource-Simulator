import React from 'react';
import FireArmadaLogo from "../images/fire_armada_logo.webp";
import "../styles/header.css";

class Header extends React.Component {
    render() {
        return (
            <div className="header">
                <img className="sponsor-logo" src={FireArmadaLogo} alt="Fire Armada Logo"/>
                
                <a className="sponsor-info" href="https://www.firearmada.com/" target="_blank">
                <button className="sponsor-info-button btn-anim">About Our Sponsor</button>
                </a>
          </div> 
        )
    }
}

export default Header;