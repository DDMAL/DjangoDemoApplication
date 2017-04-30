import React from "react";
import {
    updateCurrentQueryTerm,
    performSearch
} from "../actions/query_actions";


class SearchBar extends React.Component
{
    onInputChange (event)
    {
        console.log(event.target.value);

        updateCurrentQueryTerm(event.target.value);
        performSearch(event.target.value);
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

export default SearchBar;