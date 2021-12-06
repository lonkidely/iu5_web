import React from 'react';
import {Routes, Route} from "react-router-dom";
import MainPage from "../../pages/main/MainPage";
import Opers from "../../pages/opers/Opers";
import Langs from "../../pages/langs/Langs";
import OperDetail from "../../pages/opers/OperDetail";
import LangDetail from "../../pages/langs/LangDetail";

const Main = () => {
    return (
        <div className="flex wrapper" style={{'textAlign':'center'}}>
            <Routes>
                <Route exact path='/' element={<MainPage/>}/>
                <Route path='/opers' element={<Opers/>}/>
                <Route path='/oper/:id' element={<OperDetail/>}/>
                <Route path='/langs' element={<Langs/>}/>
                <Route path='/lang/:id' element={<LangDetail/>}/>
            </Routes>
        </div>
    );
};

export default Main;