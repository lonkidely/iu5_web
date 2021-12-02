class Urls {
    constructor() {
        this.url = 'http://127.0.0.1:8000/';
    }

    opers() {
        return `${this.url}Operator/`;
    }

    operId(id) {
        return `${this.url}Operator/${id}`;
    }

    langs() {
        return `${this.url}Proglang/`;
    }
}

export const urls = new Urls();
