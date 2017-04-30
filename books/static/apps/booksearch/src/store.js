import { createStore, applyMiddleware } from "redux";
import rootReducer from "./reducers"
import thunk from "redux-thunk";

let middlewares = [thunk];

if (process.env.NODE_ENV !== `production`) {
    const reduxLogger = require(`redux-logger`);
    const logger = reduxLogger.createLogger();
    middlewares.push(logger);
}


export default function (initialState)
{
    return createStore(
        rootReducer,
        initialState,
        applyMiddleware(...middlewares)
    )
}