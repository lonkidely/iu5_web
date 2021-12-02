import {LangList} from "../../components/langs/LangList.js";

export class Langs {
    constructor(parent) {
        this.parent = parent;
    }

    render() {
        const langs = new LangList(this.parent);
        langs.render();
    }
}