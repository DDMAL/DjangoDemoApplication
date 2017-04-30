import React from "react";
import SearchBar from "./search_bar";
import Results from "./results";


class App extends React.Component
{
    render ()
    {
        return (
            <div>
                <h3>Search Books and Authors</h3>
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