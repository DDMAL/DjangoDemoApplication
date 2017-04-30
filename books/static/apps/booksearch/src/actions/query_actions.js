import {
    UPDATE_CURRENT_QUERY_TERM
} from "../constants";

import {
    updateSearchResults
} from "./results_actions";

const SERVER_BASE_URL = "http://localhost:8000/search/";

export function performSearch (query)
{
    console.log("Performing Search for " + query);

    return (dispatch) =>
    {
        let querystring = query ? `?${query}` : "";

        return fetch(`${SERVER_BASE_URL}${querystring}`, {
            headers: {
                "Accept": "application/json"
            }
        }).then( (response) => {
            return response.json();
        }).then( (payload) => {
            return dispatch(updateSearchResults(payload))
        })
    }
}


export function updateCurrentQueryTerm (query)
{
    return {
        type: UPDATE_CURRENT_QUERY_TERM,
        query
    }
}