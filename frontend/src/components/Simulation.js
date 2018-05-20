import React, { Component } from 'react';
import classes from './Simulation.css';
import axios from 'axios';
import SimulationResults from '../containers/SimulationResults';
import SimulationForm from '../containers/SimulationForm/SimulationForm';

class Simulation extends Component {

    state = {
        results: null,
        num_games: 10,
        team1: "",
        team2: "",
        teams: [
            {code:"phi",team_name:"Philadelphia"},
            {code:"mia", team_name:"Miami"}
        ]
    }

    handleSubmit = (e) => {
        e.preventDefault();
        console.log("Handling Submit")
        axios.post('/api/simulation',{
            "team1":this.state.team1,
            "team2":this.state.team2,
            "num_games":parseInt(this.state.num_games),
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
        console.log(e.target)
        this.setState({
            team2: e.target.value,
        })
    }

    handleChange = (e) => {
        this.setState({
            num_games: e.target.value,
        })
    }

    render(){

        return (
            <div>
                <SimulationForm
                    handleSubmit={this.handleSubmit}
                    handleTeamOne={this.handleTeamOne}
                    handleTeamTwo={this.handleTeamTwo}
                    handleChange={this.handleChange}
                    num_games={this.state.num_games}
                    team1={this.state.team1}
                    team2={this.state.team2}
                    teams={this.state.teams}
                />
            {this.state.results && <SimulationResults data={this.state.results} /> }

            </div>
        )
    }
}

export default Simulation;
