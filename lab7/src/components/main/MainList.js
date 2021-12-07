import {Langs} from "../../pages/langs/Langs.js";
import {Opers} from "../../pages/opers/Opers.js";

export class MainList {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML() {
        return `
            <ul>
            <li><a href="javascript:void(0);" id="oper-link">Операторы</a></li>
            <li><a href="javascript:void(0);" id="lang-link">Языки</a></li>
            </ul>
        `;
    }

    render() {
        this.parent.insertAdjacentHTML('beforeend', this.getHTML());

        document.getElementById('oper-link').addEventListener("click", () => {
            const opers = new Opers(this.parent);
            opers.render();
        });
        document.getElementById('lang-link').addEventListener("click", () => {
            const langs = new Langs(this.parent);
            langs.render();
        });
    }


}
