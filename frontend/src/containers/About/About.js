import React from 'react';
import Nav from '../Nav/Nav';
import Header from '../Header/Header';

import classes from './About.css';

const About = () => {
    return (
        <div className={classes.About}>
            <Header>
                <Nav />
            </Header>

            <h1>About</h1>
            
            <p>Baseball Sim is a program that simulates baseball game outcomes based on statistical models and official MLB data sources.</p>
        </div>
    )
}
 
export default About;