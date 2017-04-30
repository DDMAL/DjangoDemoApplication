import React from "react";
import { connect } from "react-redux";
import {
    updateCurrentQueryTerm,
    performSearch
} from "../actions/query_actions";


class SearchBar extends React.Component
{
    onInputChange (event)
    {
        console.log(event.target.value);

        this.props.updateCurrentQueryTerm(event.target.value);
        this.props.performSearch(event.target.value);
    }

    render ()
    {
        return (
            <div>
                <input type="text"
                       placeholder="Search"
                       onChange={ event => this.onInputChange(event) }
                />
            </div>
        );
    }
}

function mapStateToProps (state)
{
    return {
        currentQuery: state.currentQuery
    }
}

const mapDispatchToProps = {
    updateCurrentQueryTerm,
    performSearch
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchBar);