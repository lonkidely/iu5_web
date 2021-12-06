import React, {useEffect, useState} from 'react';
import {useParams} from "react-router";
import {getFromServer} from "../../utils/getFromServer";

const LangDetail = () => {
    const id = useParams().id;

    const [lang, setLang] = useState();
    const [isLoaded, setIsLoaded] = useState(false);
    useEffect(() => {
        getFromServer('http://127.0.0.1:8000/Proglang/' + id.toString()).then((data) => {
            setLang(data);
            setIsLoaded(true);
        });
    }, []);

    return (
        <div className="d-flex justify-content-center m-5">
            <table style={{'border': '2px solid black'}}>
                <tr>
                    <td>ID языка:</td>
                    <td>{id}</td>
                </tr>
                <tr>
                    <td style={{'padding':'10px'}}>Название языка:</td>
                    <td>{isLoaded ? lang.title : 'загружается...'}</td>
                </tr>
            </table>
        </div>
    );
};

export default LangDetail;