import React from 'react';
import {Card} from 'react-bootstrap'
import {Link} from "react-router-dom";

const OperCard = ({id, name}) => {

    return (
        <Card className="card">
            <Card.Body>
                <div className="textStyle">
                    <Card.Title>ID = {id}</Card.Title>
                </div>
                <div className="textStyle">
                    <Card.Text>Обозначение: {name}</Card.Text>
                </div>
                <Link to={'/oper/'+id.toString()}>Подробнее</Link>
            </Card.Body>
        </Card>
    );
};

export default OperCard;