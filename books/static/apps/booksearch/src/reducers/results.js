import {
    UPDATE_SEARCH_RESULTS
} from "../constants";

const INITIAL_STATE = [];

<<<<<<< HEAD
export default function results (state = INITIAL_STATE, action)
=======

export default function results(state = INITIAL_STATE, action)
>>>>>>> resolve
{
    switch (action.type)
    {
        case (UPDATE_SEARCH_RESULTS):
            return action.results;
        default:
            return state;
    }
}