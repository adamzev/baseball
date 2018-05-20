import React from 'react';

const SimulationResult = (props) => {
    return (
        <div>
        <table style={{margin: "auto"}}>
            <thead>
                <th>Team</th>
                {props.game.innings.map(i => {
                    return (<th>{i.inning}</th>)
                })}
                <th>Score</th>
                <th>Hits</th>
            </thead>
            <tbody>
                
                <tr>
                    <td>{props.game.home_team}</td>
                    {props.game.innings.map(i => {
                        return (<td>{i.score.home}</td>)
                    })}
                    <td>{props.game.score.home}</td>
                    <td>{props.game.hits.home}</td>
                </tr>

                <tr>
                    <td>{props.game.away_team}</td>
                    {props.game.innings.map(i => {
                        return (<td>{i.score.away}</td>)
                    })}
                    <td>{props.game.score.away}</td>
                    <td>{props.game.hits.away}</td>
                </tr>
            </tbody>
        </table>
        </div>
    )
}
 
export default SimulationResult;