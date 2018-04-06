import {
    UPDATE_CURRENT_QUERY_TERM
} from "../constants";

import {
    updateSearchResults
<<<<<<< HEAD
} from "./results_actions";
=======
} from "./results_actions"

>>>>>>> resolve

const SERVER_BASE_URL = "http://localhost:8000/search/";

export function performSearch (query)
{
<<<<<<< HEAD
=======
    console.log("Performing search for " + query);

>>>>>>> resolve
    return (dispatch) =>
    {
        let querystring = query ? `?q=${query}` : "";

        return fetch(`${SERVER_BASE_URL}${querystring}`, {
            headers: {
                "Accept": "application/json"
            }
        }).then( (response) => {
            return response.json();
        }).then( (payload) => {
<<<<<<< HEAD
            return dispatch(updateSearchResults(payload))
=======
            return dispatch(updateSearchResults(payload));
>>>>>>> resolve
        })
    }
}


<<<<<<< HEAD
export function updateCurrentQueryTerm (query)
=======
export function updateQueryTerm (query)
>>>>>>> resolve
{
    return {
        type: UPDATE_CURRENT_QUERY_TERM,
        query
    }
}