export class Lang {
    constructor(parent, id) {
        this.parent = parent;
        this.id = id;
    }

    getData() {
        return {
            id: 3,
            title: "Swift - любителям яблок посвещается"
        };
    }

    get page() {
        return document.getElementById('lang');
    }

    getHTML() {
        return `
            <div id="lang" class="d-flex flex-wrap">
                
            </div>
        `
    }

    render() {
        this.parent.innerHTML = '';
        this.parent.insertAdjacentHTML('beforeend', this.getHTML());
    }
}