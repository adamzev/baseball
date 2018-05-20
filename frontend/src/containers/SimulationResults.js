import React from 'react';

import SimulationResult from './SimulationResult';

const SimulationResults = (props) => {
    const results = props.data.game_details.map((game, i) => {
        return (
            <SimulationResult key={i} index={i} game={game} />
        )
    })
    return (
        <div>
        <p>{props.data.home}</p>
        <p>{props.data.away}</p>
        {results}
        </div>
    )
}

export default SimulationResults;