import React from 'react';
import { NavLink } from 'react-router-dom';

import classes from './Nav.css';

const Nav = () => {
    return (
        <div className={classes.NavContainer}>
            <NavLink 
                to="/" 
                exact
                className={classes.Link} 
                activeClassName={classes.LinkActive}>
            Simulator
            </NavLink>
            <NavLink 
                to="/about" 
                exact
                className={classes.Link} 
                activeClassName={classes.LinkActive}>
            About
            </NavLink>
        </div>
    )
}
 
export default Nav;