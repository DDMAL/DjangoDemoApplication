import React from "react";


const BookResultType = ({resultProp}) =>
{
    return (
        <div className="book-result-type">
<<<<<<< HEAD
            <h3><a href={ `/books/${resultProp.pk}` }>{ resultProp.title_s }</a> by { resultProp.author_s } (Book)</h3>
        </div>
    )
};


const AuthorResultType = ({resultProp}) =>
{
    return (
        <div className="author-result-type">
            <h3><a href={ `/authors/${resultProp.pk}` }>{ resultProp.first_name_s } { resultProp.last_name_s }</a> (Author)</h3>
        </div>
    )
=======
            <h3><a href={ `/books/${resultProp.pk}` }>
                { resultProp.title_s }
            </a> by { resultProp.author_s } (Book)</h3>
        </div>
    );
>>>>>>> resolve
};



class Result extends React.Component
{
    _renderResultType ()
    {
        switch (this.props.result.type)
        {
<<<<<<< HEAD
            case "book":
                return <BookResultType resultProp={ this.props.result } />;
            case "author":
                return <AuthorResultType resultProp={ this.props.result } />;
=======
            case ("book"):
                return <BookResultType resultProp={ this.props.result } />;
            case ("author"):
                return "";
>>>>>>> resolve
            default:
                return <div>Unknown Result Type</div>;
        }
    }

    render ()
    {
        return (
<<<<<<< HEAD
            <div className="result-type">
                { this._renderResultType() }
            </div>
        )
    };
=======
            <div className="actual-result">
                { this._renderResultType() }
            </div>
        );
    }
>>>>>>> resolve
}

export default Result;