import './App.css';
//import {BrowserRouter as Router,Route,Switch} from 'react-router-dom'
import React from 'react'
import HeaderComponent from './components/HeaderComponent'; // adapte le chemin selon ta structure


function App() {
  return (
    <div className="App">
       <Router>
        <HeaderComponent/>
       </Router>
    </div>
  );
}


 export default App;
