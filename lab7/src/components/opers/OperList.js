import {OperCard} from "./OperCard.js";
import {MainList} from "../main/MainList.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class OperList {
    constructor(parent) {
        this.parent = parent;
        this.data = undefined
    }

    get page() {
        return document.getElementById('opers')
    }

    async getData() {
        return ajax.get(urls.opers());
    }

    getHTML() {
        return `
            <button class="btn btn-primary" id="return-back">Назад</button>
            <div id="opers" class="d-flex flex-wrap">
                
            </div>
        `
    }

    async clickBut(e){
        const cardId = e.target.dataset.id;
        const data = await ajax.get(urls.operId(cardId));
        alert(`Количество тактов = ${data.data.count_cycles}`);
    }

    async render() {
        this.parent.innerHTML = '';
        this.parent.insertAdjacentHTML('beforeend', this.getHTML());

        document.getElementById('return-back').addEventListener('click', () => {
            this.parent.innerHTML = '';
            const mainList = new MainList(this.parent);
            mainList.render();
        });

        const data = await this.getData();

        data.data.forEach((item) => {
            const oper = new OperCard(this.page);
            oper.render(item, this.clickBut.bind(this));
        })
    }
}