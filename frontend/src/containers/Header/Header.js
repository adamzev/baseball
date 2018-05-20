import React from 'react';

import Nav from '../Nav/Nav';

import classes from './Header.css';

const Header = (props) => {
    return (
        <header className={classes["App-header"]}>
        <h1 style={{ fontSize: "2em"}}><span role="img" aria-label="baseball emoji">⚾🧢🍿📊</span></h1>
        <h1 className={classes["App-title"]}>Baseball Simulator</h1>

            {props.children}

        </header>
    )
}
 
export default Header;