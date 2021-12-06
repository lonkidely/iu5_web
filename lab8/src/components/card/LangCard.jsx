import React from 'react';
import {Card} from 'react-bootstrap'
import {Link} from "react-router-dom";

const LangCard = ({id, title}) => {

    return (
        <Card className="card">
            <Card.Body>
                <div className="textStyle">
                    <Card.Title>ID = {id}</Card.Title>
                </div>
                <div className="textStyle">
                    <Card.Text>Название: {title}</Card.Text>
                </div>
                <Link to={'/lang/' + id.toString()}>Подробнее</Link>
            </Card.Body>
        </Card>
    );
};

export default LangCard;