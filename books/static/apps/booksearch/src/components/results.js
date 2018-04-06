import React from "react";
import { connect } from "react-redux";
import Result from "./result";


class Results extends React.Component
{
    render ()
    {
        if (this.props.results.length === 0)
        {
            return null;
        }

        return (
            <div>
                <h2>Results</h2>
                { this.props.results.map( (thisResult, idx) => {
                    return <Result result={ thisResult } key={ idx } />
                })}
            </div>
        );
    }
}

function mapStateToProps (state)
{
    return {
        results: state.results
    }
}

export default connect(mapStateToProps)(Results);