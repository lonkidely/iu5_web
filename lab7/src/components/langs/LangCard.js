export class LangCard {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return `
            <div class="card" style="width: 200px">
                <div class="card-body">
                    <h5 class="card-title">ID = ${data.id}</h5>
                    <p class="card-text">${data.title}</p>
                </div>
            </div>
        `;
    }

    addListeners(data, listener){
        document.getElementById(`click-card-${data.id}`).addEventListener("click", listener);
    }

    render(data) {
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML('beforeend', html);
    }
}
