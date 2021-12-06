import React, {useEffect, useState} from 'react';
import {useParams} from "react-router";
import {getFromServer} from "../../utils/getFromServer";

const OperDetail = () => {
    const id = useParams().id;

    const [oper, setOper] = useState();
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        getFromServer('http://127.0.0.1:8000/Operator/' + id.toString()).then((data) => {
            setOper(data);
            setIsLoaded(true);
        });
    }, []);

    return (
        <div className="d-flex justify-content-center m-5">
            <table style={{'border': '2px solid black'}}>
                <tr>
                    <td>ID оператора:</td>
                    <td>{id}</td>
                </tr>
                <tr>
                    <td style={{'padding':'10px'}}>Обозначение оператора:</td>
                    <td>{isLoaded ? oper.name : 'загружается...'}</td>
                </tr>
                <tr>
                    <td>Количество тактов ЦП:</td>
                    <td>{isLoaded ? oper.count_cycles : 'загружается...'}</td>
                </tr>
            </table>
        </div>
    );
};

export default OperDetail;