import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './App.css';
import Simulation from './components/Simulation';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 style={{ fontSize: "2em"}}>⚾🧢🍿📊</h1>
          <h1 className="App-title">Baseball Simulator</h1>
          <Link to="/about">About</Link>
        </header>
        <Simulation />
      </div>
    );
  }
}

export default App;
