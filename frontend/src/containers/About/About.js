import React from 'react';
import { Link } from 'react-router-dom';

import '../../App.css';

const About = () => {
    return (
        <div className="App">
            <header className="App-header">
            <h1 style={{ fontSize: "2em"}}>⚾🧢🍿📊</h1>
            <h1 className="App-title">Baseball Simulator</h1>
            </header>
            <h1>About</h1>
            <Link to="/">Simulator</Link>
            <p>Baseball Sim is a program that simulates baseball game outcomes based on statistical models and official MLB data sources.</p>
        </div>
    )
}
 
export default About;