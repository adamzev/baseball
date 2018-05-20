import React from 'react';
// import SelectField from 'material-ui/core/SelectField';
// import MenuItem from 'material-ui/core/MenuItem';

import classes from './SimulationForm.css';

const SimulationForm = (props) => {
    const teams = props.teams.map((team, i) => {
        return (
            <option value={team.code} key={i}>{team.team_name}</option>
        )
    })
    return (
        <form className={classes.SimulationForm}>
        <p>Team 1: {props.team1.code}</p>
        <div className={classes.TeamSelect}>
            <select required name="team1" value={props.team1.code} onChange={props.handleTeamOne}>
                <option value="">Select Team 1</option>
                {teams}
            </select>
        </div>
        <p>Team 2: {props.team2.code}</p>
        <div className={classes.TeamSelect}>
            <select required name="team2" value={props.team2.code} onChange={props.handleTeamTwo}>
                <option value="">Select Team 2</option>
                {teams}
            </select>
        </div>
        <p>Number of Games:</p>
        <input className={classes.NumGames} type="number" value={props.num_games} onChange={props.handleChange} />
        <br /><br />
        <button className={classes.RunSimulation} onClick={props.handleSubmit}>Run Simulation</button>
    </form>
    )
}
 
export default SimulationForm;