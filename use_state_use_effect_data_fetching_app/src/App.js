
import {useState,useEffect} from "react";
import Main from "./components/main/Main";
import Header from "./components/header/Header";

function App() {
  const [user,setUser]=useState("");
  const getData=()=>{
    fetch("https://randomuser.me/api/")
  .then((res) => res.json())
  .then((data) => setUser(data.results[0]));
  };
  
  useEffect(()=>{
   // ?componentDidMount
   getData();
  },[]);

  
  return (
    <div className="app">
      <Header user={user} />
      <Main {...user} getData={getData}/>
    </div>
  );
}

export default App;
