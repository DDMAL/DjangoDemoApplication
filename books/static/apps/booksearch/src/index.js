import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import App from "./components/app";
import configureStore from "./store";

<<<<<<< HEAD
let INITIAL_STATE = {};

let myStore = configureStore(INITIAL_STATE);
=======

let myStore = configureStore({});
>>>>>>> resolve

ReactDOM.render(
    <Provider store={ myStore }>
        <App />
    </Provider>,
    document.getElementById('content')
);