import React from "react";
import "./Main.css";
const Main =({picture,name,email,phone,location,registred,getData})=>{
    console.log(picture,name,email,phone,location,registred);
    return (
    <div className="cardWrapper">
        <div className="cardMain">
            <div className="cardHeader">
                <img src={picture?.large} alt="img"/>
                <h1>{name?.first} {name?.last}{" "}</h1>
            </div>
            <div className="cardMiddle">
                <h3>{email}</h3>
                <h3>{phone}</h3>
                <h3>{location?.city}/{location?.country}</h3>
            </div>
            <div className="cardFooter"></div>
            <p>Age:{registred?.age}</p>
            <p>{new Date(registred?.date).toLocaleDateString()}</p>
        </div>
        <button onClick={getData}>Get Data</button>
    </div>
);
}
export default Main;