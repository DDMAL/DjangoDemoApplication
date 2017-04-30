import React from "react";
import SearchBar from "./search_bar";
import Results from "./results";


class App extends React.Component
{
    render ()
    {
        return (
            <div>
                <div className="page-header">
                    <SearchBar />
                </div>
                <div className="page-results">
                    <Results />
                </div>

            </div>
        )
    }
}

export default App;