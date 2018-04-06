import { createStore, applyMiddleware } from "redux";
<<<<<<< HEAD
import rootReducer from "./reducers"
import thunk from "redux-thunk";

let middlewares = [thunk];

if (process.env.NODE_ENV !== `production`) {
    const reduxLogger = require(`redux-logger`);
=======
import rootReducer from "./reducers";
import thunk from "redux-thunk";


let middlewares = [thunk];

if (process.env.NODE_ENV !== "production")
{
    const reduxLogger = require('redux-logger');
>>>>>>> resolve
    const logger = reduxLogger.createLogger();
    middlewares.push(logger);
}

<<<<<<< HEAD

=======
>>>>>>> resolve
export default function (initialState)
{
    return createStore(
        rootReducer,
        initialState,
        applyMiddleware(...middlewares)
    )
<<<<<<< HEAD
}
=======
}
>>>>>>> resolve
