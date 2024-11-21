import React, { useEffect,useState } from "react";

const Effect=({props})=>{
    const [count,setCount]= useState(0);

    // useEffect(()=>{
    //     console.log("Mountin + Updating");
    //     setTimeout(()=>{
    //         alert("Data Fetched");
    //     },1000);
    // },[count]);

    const fetchData=()=>{
        console.log("Clean-up");
    }

    useEffect(()=>{
        
        console.log("Mounting");
        const timerId=setInterval(fetchData,1000);
        return ()=>{

            clearInterval(timerId);
            console.log("Unmounting");
        }
    },[count,props]);
    console.log("Render");
    
    return (
    <div>
        <h3>{count}</h3>
        <button onClick={()=>setCount((count)=>count+1)}>Click</button>
    </div>
    );
};

export default Effect;