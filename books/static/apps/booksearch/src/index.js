import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import App from "./components/app";
import configureStore from "./store";


let myStore = configureStore({});

ReactDOM.render(
    <Provider store={ myStore }>
        <App />
    </Provider>,
    document.getElementById('content')
);