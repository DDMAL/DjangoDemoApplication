import React from "react";
import { connect } from "react-redux";
import {
<<<<<<< HEAD
    updateCurrentQueryTerm,
=======
    updateQueryTerm,
>>>>>>> resolve
    performSearch
} from "../actions/query_actions";


class SearchBar extends React.Component
{
    onInputChange (event)
    {
<<<<<<< HEAD
        console.log(event.target.value);

        this.props.updateCurrentQueryTerm(event.target.value);
=======
        this.props.updateQueryTerm(event.target.value);
>>>>>>> resolve
        this.props.performSearch(event.target.value);
    }

    render ()
    {
        return (
            <div>
                <input type="text"
                       placeholder="Search"
<<<<<<< HEAD
                       onChange={ event => this.onInputChange(event) }
                />
            </div>
        );
=======
                       value={ this.props.myQuery }
                       onChange={ (event) => this.onInputChange(event) } />
            </div>
        )
>>>>>>> resolve
    }
}

function mapStateToProps (state)
{
    return {
<<<<<<< HEAD
        currentQuery: state.currentQuery
    }
}

const mapDispatchToProps = {
    updateCurrentQueryTerm,
    performSearch
};
=======
        myQuery: state.currentQuery
    };
}

const mapDispatchToProps = {
    updateQueryTerm,
    performSearch
}
>>>>>>> resolve

export default connect(mapStateToProps, mapDispatchToProps)(SearchBar);