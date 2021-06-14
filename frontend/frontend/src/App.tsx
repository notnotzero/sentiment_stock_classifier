import React from 'react';
import './App.css';
import Search from './Search/Search'
import 'bootstrap/dist/css/bootstrap.min.css';
import NavComponent from './Nav/Nav'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import Results from './Results/Results'

function App() {
  return (
    <Router>
    <div className="App">
      <NavComponent />
      <div style={{ display : 'flex', justifyContent: 'center'}}>

      <Switch>
          <Route path="/home">
            <Search />
          </Route>
          <Route path="/result">
            <Results />
          </Route>
          <Route path="/">
            <Search />
          </Route>
        </Switch>
      
      </div>
    </div>
    </Router>
    
  );
}

export default App;
