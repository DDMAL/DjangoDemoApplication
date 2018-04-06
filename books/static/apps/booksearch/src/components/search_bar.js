import React from "react";
import { connect } from "react-redux";
import {
    updateQueryTerm,
    performSearch
} from "../actions/query_actions";


class SearchBar extends React.Component
{
    onInputChange (event)
    {
        this.props.updateQueryTerm(event.target.value);
        this.props.performSearch(event.target.value);
    }

    render ()
    {
        return (
            <div>
                <input type="text"
                       placeholder="Search"
                       value={ this.props.myQuery }
                       onChange={ (event) => this.onInputChange(event) } />
            </div>
        )
    }
}

function mapStateToProps (state)
{
    return {
        myQuery: state.currentQuery
    };
}

const mapDispatchToProps = {
    updateQueryTerm,
    performSearch
}

export default connect(mapStateToProps, mapDispatchToProps)(SearchBar);