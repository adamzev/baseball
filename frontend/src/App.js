import React, { Component } from 'react';
import Simulation from './components/Simulation';
import Nav from './containers/Nav/Nav';
import Header from './containers/Header/Header';

class App extends Component {
  render() {
    return (
      <div>
        <Header>
          <Nav />
        </Header>
        <Simulation />
      </div>
    );
  }
}

export default App;
