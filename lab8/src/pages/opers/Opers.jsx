import React, {useState} from 'react';
import {Button, Row, Col} from "react-bootstrap";
import OperCard from "../../components/card/OperCard";
import useWindowSize from "../../utils/useWindowSize";
import {getFromServer} from "../../utils/getFromServer";

const Opers = () => {

    const [opers, setOpers] = useState([]);

    const loadOpers = async () => {
        const results = await getFromServer('http://127.0.0.1:8000/Operator/');
        await setOpers(results);
        document.getElementById("loadButton").hidden = true;
    }

    const {width} = useWindowSize();
    const isMobile = width && width <= 600;

    return (
        <div className="d-flex flex-column container justify-content-center">
            <div className="m-5" id="loadButton">
                <Button onClick={loadOpers}>Загрузить список операторов</Button>
            </div>
            <div className="mb-5">
                <Row xs={1} md={isMobile ? 1 : 3} className="g-3">
                    {opers.map((item, index) => {
                        return <Col>
                            <OperCard {...item} key={index}/>
                        </Col>
                    })}
                </Row>
            </div>
        </div>
    );
};

export default Opers;