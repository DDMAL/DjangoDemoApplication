import { combineReducers } from "redux";
import currentQuery from "./current_query";
import results from "./results";


const rootReducer = combineReducers({
    currentQuery,
    results
});

export default rootReducer;