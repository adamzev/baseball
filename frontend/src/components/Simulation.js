import React, { Component } from 'react';

import axios from 'axios';
import SimulationResults from '../containers/SimulationResults';

class Simulation extends Component {

    state = {
        results: null,
        team1: "", 
        team2: "",
    }

    handleSubmit = (e) => {
        e.preventDefault();
        console.log("Handling Submit")
        axios.post('/api/simulation',{
            "team1":this.state.team1,
            "team2":this.state.team2,
            "num_games":5
        })
            .then( (response) => {
                console.log(response)
                this.setState({
                    results:response.data
                })
            })
    }

    handleTeamOne = (e) => {
        this.setState({
            team1: e.target.value,
        })
    }

    handleTeamTwo = (e) => {
        this.setState({
            team2: e.target.value,
        })
    }

    render(){

        return (
            <div>
            <form>
                <p>Team 1: {this.state.team1}</p>
                <select onChange={this.handleTeamOne}>
                    <option>Select Team 1</option>
                    <option value="phi">Philadelphia</option>
                    <option value="mia">Miami</option>
                </select>
                <p>Team 2: {this.state.team2}</p>
                <select value={this.state.team2} onChange={this.handleTeamTwo}>
                    <option>Select Team 2</option>
                    <option value="phi">Philadelphia</option>
                    <option value="mia">Miami</option>
                </select>
                <br /><br />
                <button onClick={this.handleSubmit}>Run Simulation</button>
            </form>
            <h1>Simulation Results</h1>
            <p>{this.state.results && <SimulationResults data={this.state.results} /> }</p>
            </div>
        )
    }
}

export default Simulation;
