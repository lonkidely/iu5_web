import {LangCard} from "./LangCard.js";
import {MainList} from "../main/MainList.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class LangList {
    constructor(parent) {
        this.parent = parent;
    }

    get page() {
        return document.getElementById('langs')
    }

    async getData() {
        return ajax.get(urls.langs());
    }

    getHTML() {
        return `
            <button class="btn btn-primary" id="return-back">Назад</button>
            <div id="langs" class="d-flex flex-wrap">
                
            </div>
        `
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
            const lang = new LangCard(this.page);
            lang.render(item);
        })
    }
}
