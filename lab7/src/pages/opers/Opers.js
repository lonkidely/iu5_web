import {OperList} from "../../components/opers/OperList.js";

export class Opers {
    constructor(parent) {
        this.parent = parent;
    }

    render() {
        const opers = new OperList(this.parent);
        opers.render();
    }
}