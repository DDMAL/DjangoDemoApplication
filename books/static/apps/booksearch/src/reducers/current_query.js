import {
    UPDATE_CURRENT_QUERY_TERM,
    CLEAR_CURRENT_QUERY
} from "../constants";

const INITIAL_STATE = "";


<<<<<<< HEAD
export default function currentQuery (state = INITIAL_STATE, action)
=======
export default function currentQuery(state = INITIAL_STATE, action)
>>>>>>> resolve
{
    switch (action.type)
    {
        case (UPDATE_CURRENT_QUERY_TERM):
            return action.query;
        case (CLEAR_CURRENT_QUERY):
            return INITIAL_STATE;
        default:
            return state;
    }
}