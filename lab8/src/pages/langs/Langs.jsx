import React, {useState} from 'react';
import useWindowSize from "../../utils/useWindowSize";
import {Button, Col, Row} from "react-bootstrap";
import LangCard from "../../components/card/LangCard";
import {getFromServer} from "../../utils/getFromServer";

const Langs = () => {

    const [langs, setLangs] = useState([]);
    const [isLoaded, setIsLoaded] = useState(false);

    const loadLangs = async () => {
        const results = await getFromServer('http://127.0.0.1:8000/Proglang/');
        await setLangs(results);
        await setIsLoaded(true);
        document.getElementById("loadButton").hidden = true;
    }

    const {width} = useWindowSize();
    const isMobile = width && width <= 600;

    return (
        <div className="d-flex flex-column container justify-content-center">
            <div className="m-5" id="loadButton">
                <Button onClick={loadLangs}>Загрузить список языков</Button>
            </div>
            <div className="mb-5">
                <Row xs={1} md={isMobile ? 1 : 3} className="g-3">
                    {isLoaded ? langs.map((item, index) => {
                        return <Col>
                            <LangCard {...item} key={index}/>
                        </Col>
                    }) : ''}
                </Row>
            </div>
        </div>
    );
};

export default Langs;