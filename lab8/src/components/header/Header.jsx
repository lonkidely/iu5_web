import React from 'react';
import {Link} from "react-router-dom";

const Header = () => {
    return (
        <nav>
            <div className="container d-flex justify-content-center mb-1">
                <ul className="nav nav-tabs">
                    <li className="nav-item"><Link className="nav-link" to='/'>Главная</Link></li>
                    <li className="nav-item"><Link className="nav-link" to='/opers'>Операторы</Link></li>
                    <li className="nav-item"><Link className="nav-link" to='/langs'>Языки программирования</Link></li>
                </ul>
            </div>
        </nav>
    );
};

export default Header;